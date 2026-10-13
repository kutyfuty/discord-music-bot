"""
Help, language and presence for the music bot.

/yardim (/help, !yardim) — music commands; /dil (/language) — server language (tr / en, admins).
"""
import discord
from discord import app_commands
from discord.ext import commands, tasks

from database import sunucu_dil_ayarla, yonetici_mi
from dil import _t, dil_zorla
from yapilandirma import MUZIK_ORNEKLERI, PREFIX

BOLUMLER = [
    ("🎵 Çalma", [
        ("oynat <şarkı / link>", "YouTube, YouTube Music, Spotify, SoundCloud ya da doğrudan link çalar"),
        ("siradaki <şarkı>", "Şarkıyı kuyruğun başına ekler"),
        ("atla · onceki · oylaatla", "Sonraki / önceki şarkı, oylamalı atlama"),
        ("duraklat · devam · durdur", "Duraklat, sürdür, durdur ve kuyruğu temizle"),
        ("sar 1:30 · ileri 10 · geri 10", "Şarkıda ileri / geri sar"),
    ]),
    ("📜 Kuyruk", [
        ("kuyruk · simdi", "Kuyruğu ve çalan şarkıyı gösterir"),
        ("kaldir · tasi · karistir · temizle", "Kuyruğu düzenle"),
        ("dongu · otomatik", "Tekrar modu ve otomatik oynatma (radyo)"),
    ]),
    ("🎚️ Ses", [
        ("ses 0-150 · normalizasyon", "Ses seviyesi ve ses dengeleme"),
        ("katil · cik", "Odaya çağır / odadan çıkar"),
    ]),
    ("💾 Listeler ve ayarlar", [
        ("calmalistesi", "Kişisel çalma listelerin (kaydet, ekle, oynat, sil)"),
        ("muzikayar", "DJ rolü, 7/24 modu, istek kanalı, zaman aşımı (yönetici)"),
        ("dil tr | en", "Botun bu sunucudaki dili (yönetici)"),
    ]),
]


class Yardim(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._i = 0

    async def cog_load(self):
        self.durum.start()

    async def cog_unload(self):
        self.durum.cancel()

    @tasks.loop(seconds=30)
    async def durum(self):
        muzik = self.bot.get_cog("Muzik")
        calan = muzik.aktif_oynatici_sayisi() if muzik else 0
        metinler = ["/oynat · /yardim", f"🎶 {calan}" if calan else "/help"]
        try:
            await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening,
                                                                     name=metinler[self._i % len(metinler)]))
        except Exception:
            pass
        self._i += 1

    @durum.before_loop
    async def _hazir(self):
        await self.bot.wait_until_ready()

    def _embed(self):
        e = discord.Embed(title=_t("🎶 {bot} — müzik komutları", bot=self.bot.user.display_name), color=0xE8A33D,
                          description=_t("Bir ses kanalına gir ve `/oynat <şarkı>` ya da `{prefix}oynat <şarkı>` yaz.", prefix=PREFIX))
        for baslik, satirlar in BOLUMLER:
            e.add_field(name=_t(baslik), value="\n".join(f"`/{k}` — {_t(a)}" for k, a in satirlar), inline=False)
        if len(MUZIK_ORNEKLERI) > 1:
            e.add_field(name=_t("🎧 Birden çok müzik botu"), inline=False, value=_t(
                "Bu sunucuda birden çok müzik botu var: `{prefix}oynat` yazınca **senin** ses kanalındaki bot cevap verir, "
                "odanda bot yoksa boştaki gelir.", prefix=PREFIX))
        return e

    @commands.hybrid_command(name="yardim", aliases=["help", "komutlar", "commands"], description="Müzik komutlarını gösterir")
    async def yardim(self, ctx):
        await ctx.send(embed=self._embed(), ephemeral=True) if ctx.interaction else await ctx.send(embed=self._embed())

    @commands.hybrid_command(name="dil", aliases=["language", "lang"], description="Botun bu sunucudaki dili (tr / en)")
    @app_commands.describe(yeni_dil="tr / en")
    @app_commands.choices(yeni_dil=[app_commands.Choice(name="🇹🇷 Türkçe", value="tr"),
                                    app_commands.Choice(name="🇬🇧 English", value="en")])
    @app_commands.default_permissions(manage_guild=True)
    @commands.guild_only()
    async def dil(self, ctx, yeni_dil: str = "tr"):
        if not yonetici_mi(ctx.author):
            raise commands.CheckFailure()
        dil_zorla(sunucu_dil_ayarla(ctx.guild.id, yeni_dil))
        await ctx.send(_t("✅ Sunucu dili **Türkçe** olarak ayarlandı. Bot bu sunucuda artık Türkçe yanıt verecektir."))


async def setup(bot):
    await bot.add_cog(Yardim(bot))
