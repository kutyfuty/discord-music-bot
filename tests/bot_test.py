"""
Offline test — never connects to Discord, uses a temporary database.

Run: venv/bin/python tests/bot_test.py

1. main.py imports without side effects; the music + help cogs load into an offline bot and unload cleanly.
2. Every _t("…") text in the code has an English translation (dil_en.py).
3. BOT_INSTANCE=2 uses its own token file, lock, log and database.
4. Two music bots: for a prefix command exactly one bot answers — the one in the user's voice channel, else a free one.
"""
import ast
import asyncio
import glob
import json
import os
import subprocess
import sys
import tempfile
import types

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, KOK)
os.environ["BOT_DB"] = os.path.join(tempfile.mkdtemp(prefix="musicbot_test_"), "test.db")

import discord  # noqa: E402
from discord.ext import commands  # noqa: E402

GECTI = 0


def ok(kosul, mesaj):
    global GECTI
    if not kosul:
        raise AssertionError(mesaj)
    GECTI += 1
    print("  ✓", mesaj)


async def yukle():
    print("Cogs:")
    import main
    from database import veritabanini_kur
    veritabanini_kur()
    ok(main.vagonlar == ["cogs.muzik", "cogs.yardim"], "main.py: only the music and help cogs")
    b = commands.Bot(command_prefix="!", intents=discord.Intents.default(), help_command=None)   # as in main.py
    async with b:   # sets up the client so background loops can wait for "ready" without errors
        for v in main.vagonlar:
            await b.load_extension(v)
        adlar = {c.name for c in b.commands}
        ok({"oynat", "atla", "kuyruk", "yardim", "dil", "calmalistesi", "muzikayar"} <= adlar, f"{len(adlar)} commands registered")
        for v in reversed(main.vagonlar):
            await b.unload_extension(v)
        ok(not b.cogs, "cogs unload cleanly")


def ceviriler():
    print("Translations:")
    from dil_en import EN
    eksik = []
    for yol in glob.glob(os.path.join(KOK, "**", "*.py"), recursive=True):
        if "/tests/" in yol or "/venv/" in yol:
            continue
        for d in ast.walk(ast.parse(open(yol, encoding="utf-8").read())):
            if isinstance(d, ast.Call) and getattr(d.func, "id", None) == "_t" and d.args and isinstance(d.args[0], ast.Constant):
                if isinstance(d.args[0].value, str) and d.args[0].value not in EN:
                    eksik.append(f"{os.path.relpath(yol, KOK)}: {d.args[0].value[:60]}")
    from cogs.yardim import BOLUMLER
    for baslik, satirlar in BOLUMLER:
        eksik += [m for m in [baslik] + [a for _, a in satirlar] if m not in EN]
    ok(not eksik, "every reply has an English translation" + ("" if not eksik else ":\n    " + "\n    ".join(eksik)))


def ikinci_ornek():
    print("Second instance:")
    kod = ("import json, os, yapilandirma as y; print(json.dumps({'k': os.path.basename(y.KILIT_DOSYA), 'l': os.path.basename(y.LOG_DOSYA),"
           "'e': os.path.basename(y.PROFIL_ENV_DOSYA or ''), 'd': os.path.basename(y.DB_DOSYA), 'p': y.MUZIK_PROFILI}))")
    ortam = {k: v for k, v in os.environ.items() if k != "BOT_DB"}
    bir = json.loads(subprocess.run([sys.executable, "-c", kod], cwd=KOK, env=ortam, capture_output=True, text=True, check=True).stdout)
    iki = json.loads(subprocess.run([sys.executable, "-c", kod], cwd=KOK, env=dict(ortam, BOT_INSTANCE="2"),
                                    capture_output=True, text=True, check=True).stdout)
    ok(bir == {"k": "bot.lock", "l": "musicbot.log", "e": "", "d": "musicbot.db", "p": False}, "instance 1: bot.lock, musicbot.db, .env")
    ok(iki == {"k": "bot-2.lock", "l": "musicbot-2.log", "e": ".env.2", "d": "musicbot-2.db", "p": True},
       "BOT_INSTANCE=2: bot-2.lock, musicbot-2.db, token from .env.2")


async def yonlendirme():
    print("Two bots in one server:")
    from cogs.muzik import ornekler
    A, B = 1001, 1002
    ornekler.MUZIK_ORNEKLERI = [A, B]

    class Kanal:
        def __init__(self, ad, botlar=(), insan=False):
            self.name, self.voice_states = ad, {i: 1 for i in botlar}
            self.members = [types.SimpleNamespace(id=i, bot=True) for i in botlar] + ([types.SimpleNamespace(id=7, bot=False)] if insan else [])
            if insan:
                self.voice_states[7] = 1

    class Sunucu:
        id = 1
        stage_channels = []

        def __init__(self, kanallar):
            self.voice_channels = kanallar

        def get_member(self, i):
            return types.SimpleNamespace(display_name=str(i))

    async def kim(kanallar, oda):
        u = types.SimpleNamespace(id=42, bot=False, voice=types.SimpleNamespace(channel=oda))
        oda.voice_states[42] = 1
        cevap = []
        for b in (A, B):
            cog = types.SimpleNamespace(bot=types.SimpleNamespace(user=types.SimpleNamespace(id=b)))
            ctx = types.SimpleNamespace(guild=Sunucu(kanallar), author=u, interaction=None, command=types.SimpleNamespace(qualified_name="oynat"))
            try:
                await ornekler.denetle(cog, ctx)
                cevap.append(b)
            except ornekler.BaskaOrnekte:
                pass
        return cevap

    v1, v2 = Kanal("1"), Kanal("2")
    ok(await kim([v1, v2], v1) == [A], "both free → only bot 1 answers")
    v1, v2 = Kanal("1", [A], True), Kanal("2")
    ok(await kim([v1, v2], v2) == [B], "bot 1 busy in room 1 → bot 2 comes to room 2")
    v1, v2 = Kanal("1", [A], True), Kanal("2", [B], True)
    ok(await kim([v1, v2], v2) == [B], "command from room 2 → only the bot in room 2")


asyncio.run(yukle())
ceviriler()
ikinci_ornek()
asyncio.run(yonlendirme())
print(f"\nALL CHECKS PASSED ✅ ({GECTI})")
