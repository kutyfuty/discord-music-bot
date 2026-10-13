"""
Discord music bot — entry point.

Run: venv/bin/python main.py        (second instance for a second voice channel: BOT_INSTANCE=2 venv/bin/python main.py)
Importing this module has no side effects (lock / logging / token checks only happen in baslat()).
"""
import asyncio
import fcntl
import logging
import logging.handlers
import os
import signal
import ssl
import sys

import aiohttp
import discord
from discord import app_commands
from discord.ext import commands

from yapilandirma import ENV_DOSYA, GECICI_DIZIN, KILIT_DOSYA, LOG_DOSYA, PREFIX, PROFIL_ENV_DOSYA, SAHIP_ID
from database import veritabanini_kur
from dil import DilAgaci, DilCevirmeni, _t, kancalari_kur

try:
    import certifi
except ImportError:
    certifi = None

logger = logging.getLogger('MusicBot')

KILIT_CIKIS_KODU = 3           # another instance with the same lock is running (systemd: do not restart)
YAPILANDIRMA_CIKIS_KODU = 78   # EX_CONFIG — e.g. empty DISCORD_TOKEN or privileged intents disabled
_kilit_dosyasi = None


def loglari_kur():
    bicim = logging.Formatter('%(asctime)s [%(levelname)s] %(name)s: %(message)s')
    konsol = logging.StreamHandler()
    dosya = logging.handlers.RotatingFileHandler(LOG_DOSYA, maxBytes=5 * 1024 * 1024, backupCount=3, encoding='utf-8')
    for h in (konsol, dosya):
        h.setFormatter(bicim)
    logging.basicConfig(level=logging.INFO, handlers=[konsol, dosya])


def tek_ornek_kilidi_al():
    """flock: the kernel releases the lock if the process dies, no stale PID files."""
    global _kilit_dosyasi
    dosya = open(KILIT_DOSYA, "a+", encoding="utf-8")
    try:
        fcntl.flock(dosya.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError:
        logger.critical(f"The bot is already running (lock: {KILIT_DOSYA})")
        sys.exit(KILIT_CIKIS_KODU)
    dosya.seek(0)
    dosya.truncate()
    dosya.write(str(os.getpid()))
    dosya.flush()
    _kilit_dosyasi = dosya


intents = discord.Intents.default()
intents.message_content = True   # [PRIVILEGED] prefix commands and the song request channel
intents.members = True           # [PRIVILEGED] who is listening in the voice channel

kancalari_kur()   # buttons / modals / events answer in the server's language
bot = commands.Bot(command_prefix=PREFIX, intents=intents, help_command=None, owner_id=SAHIP_ID,
                   chunk_guilds_at_startup=False, tree_cls=DilAgaci)
vagonlar = ['cogs.muzik', 'cogs.yardim']


@bot.event
async def on_ready():
    if not getattr(bot, '_hazir', False):
        bot._hazir = True
        try:
            logger.info(f"{len(await bot.tree.sync())} slash commands synced globally.")
        except Exception as e:
            logger.error(f"Slash sync error: {e}")
    logger.info(f'{bot.user} ready: {len(bot.guilds)} servers')


@bot.event
async def on_command_error(ctx, error):
    from cogs.muzik.ornekler import BaskaOrnekte
    if isinstance(error, (BaskaOrnekte, commands.CommandNotFound)):
        return   # another music bot took the command / not ours: stay silent
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(_t("⏳ Yavaşla! Bu komut soğuma süresinde. **{kalan} saniye** sonra tekrar deneyebilirsin.", kalan=int(error.retry_after)), delete_after=7)
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(_t("⚠️ Eksik parametre: `{name}`. Kullanım için `{PREFIX}yardim` yaz.", name=error.param.name, PREFIX=PREFIX), delete_after=7)
    elif isinstance(error, commands.NoPrivateMessage):
        await ctx.send(_t("❌ Bu komut sadece sunucularda kullanılabilir."), delete_after=10)
    elif isinstance(error, commands.NotOwner):
        await ctx.send(_t("🚫 Bu komut sadece bot sahibine özel."), delete_after=5)
    elif isinstance(error, commands.CheckFailure):
        await ctx.send(_t("🚫 Bu komutu kullanmak için yetkin yok (Yönetici yetkisi gereklidir)."), delete_after=5)
    else:
        logger.error(f"Command error ({ctx.command}): {error}", exc_info=True)
        try:
            await ctx.send(_t("⚠️ Beklenmedik bir hata oluştu. Lütfen tekrar dene."), delete_after=7)
        except discord.HTTPException:
            pass


@bot.tree.error
async def on_tree_error(interaction: discord.Interaction, error: app_commands.AppCommandError):
    from cogs.muzik.ornekler import OrnekYonlendirme
    if isinstance(error, OrnekYonlendirme):
        mesaj = str(error)   # wrong music bot picked → tell the user which one plays in their channel
    elif isinstance(error, app_commands.CommandOnCooldown):
        mesaj = _t("⏳ Yavaşla! Bu komut soğuma süresinde. **{kalan} saniye** sonra tekrar deneyebilirsin.", kalan=int(error.retry_after))
    elif isinstance(error, (app_commands.MissingPermissions, app_commands.CheckFailure)):
        mesaj = _t("🚫 Bu komutu kullanmak için yetkin yok (Yönetici yetkisi gereklidir).")
    elif isinstance(error, app_commands.NoPrivateMessage):
        mesaj = _t("❌ Bu komut sadece sunucularda kullanılabilir.")
    else:
        logger.error(f"Slash command error: {error}", exc_info=True)
        mesaj = _t("⚠️ İşlem sırasında beklenmedik bir hata oluştu. Lütfen tekrar dene.")
    try:
        if interaction.response.is_done():
            await interaction.followup.send(mesaj, ephemeral=True)
        else:
            await interaction.response.send_message(mesaj, ephemeral=True)
    except discord.HTTPException:
        pass


async def main(token):
    ssl_ctx = ssl.create_default_context()
    if certifi:
        ssl_ctx.load_verify_locations(certifi.where())
    bot.http.connector = aiohttp.TCPConnector(ssl=ssl_ctx, force_close=True, enable_cleanup_closed=True)
    loop = asyncio.get_running_loop()
    for s in (signal.SIGTERM, signal.SIGINT):
        loop.add_signal_handler(s, lambda: asyncio.create_task(bot.close()))
    async with bot:
        await bot.tree.set_translator(DilCevirmeni())
        for vagon in vagonlar:
            await bot.load_extension(vagon)
            logger.info(f"Loaded: {vagon}")
        await bot.start(token)


def baslat():
    loglari_kur()
    tek_ornek_kilidi_al()
    token = (os.getenv("DISCORD_TOKEN") or "").strip()
    if not token:
        logger.critical(f"DISCORD_TOKEN is empty — put your bot token in {PROFIL_ENV_DOSYA or ENV_DOSYA}")
        sys.exit(YAPILANDIRMA_CIKIS_KODU)
    os.makedirs(GECICI_DIZIN, exist_ok=True)
    veritabanini_kur()
    try:
        asyncio.run(main(token))
    except discord.PrivilegedIntentsRequired:
        logger.critical("Enable 'Server Members Intent' and 'Message Content Intent' in the Discord Developer Portal → Bot.")
        sys.exit(YAPILANDIRMA_CIKIS_KODU)
    # yt-dlp was updated → exit code 75, the service manager restarts with the new version
    if getattr(bot, 'cikis_kodu', 0):
        sys.exit(bot.cikis_kodu)


if __name__ == "__main__":
    baslat()
