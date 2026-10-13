"""
Music bot configuration. Every path is resolved relative to the bot directory.

- .env        → secrets (DISCORD_TOKEN, optional SPOTIFY_CLIENT_ID / SPOTIFY_CLIENT_SECRET)
- config.json → non-secret settings (prefix, owner id, music_instances)

Second instance (two voice channels at once): run the same code with BOT_INSTANCE=2. It reads its token from
.env.2 and keeps its own lock, log and database, so both bots can run side by side. See cogs/muzik/ornekler.py.
"""
import json
import logging
import os
import shutil

from dotenv import load_dotenv

logger = logging.getLogger('MusicBot.Config')

# ── Instance ──
ORNEK = (os.getenv("BOT_INSTANCE") or "").strip()
MUZIK_PROFILI = ORNEK not in ("", "1")          # secondary instance: does not self-update yt-dlp

# ── Paths ──
BOT_DIZINI = os.path.dirname(os.path.abspath(__file__))
ENV_DOSYA = os.path.join(BOT_DIZINI, ".env")
PROFIL_ENV_DOSYA = os.path.join(BOT_DIZINI, f".env.{ORNEK}") if MUZIK_PROFILI else None
CONFIG_DOSYA = os.path.join(BOT_DIZINI, "config.json")
VERI_DIZINI = os.path.join(BOT_DIZINI, "data")
GECICI_DIZIN = os.path.join(VERI_DIZINI, "tmp")
YTDL_CACHE_DIZINI = os.path.join(VERI_DIZINI, ".ytdl_cache")
_ek = f"-{ORNEK}" if MUZIK_PROFILI else ""
LOG_DOSYA = os.path.join(BOT_DIZINI, f"musicbot{_ek}.log")
KILIT_DOSYA = os.path.join(BOT_DIZINI, f"bot{_ek}.lock")

if PROFIL_ENV_DOSYA:
    load_dotenv(PROFIL_ENV_DOSYA, override=False)   # this instance's DISCORD_TOKEN
load_dotenv(ENV_DOSYA, override=False)              # shared keys (Spotify)

DB_DOSYA = os.path.abspath(os.getenv("BOT_DB") or os.path.join(VERI_DIZINI, f"musicbot{_ek}.db"))


def _config_oku():
    try:
        with open(CONFIG_DOSYA, encoding="utf-8") as f:
            veri = json.load(f)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError as e:
        logger.critical(f"config.json is not valid JSON: {e}")
        raise SystemExit(78)
    return veri if isinstance(veri, dict) else {}


def _id(deger):
    try:
        return int(str(deger).strip()) or None
    except (TypeError, ValueError):
        return None


_config = _config_oku()
PREFIX = str(_config.get("prefix") or "!")
SAHIP_ID = _id(_config.get("owner_id"))
# Bot accounts running this code, in priority order (empty = single bot). Example: ["<bot 1 id>", "<bot 2 id>"]
MUZIK_ORNEKLERI = [i for i in (_id(x) for x in _config.get("music_instances") or []) if i]


def _calistirilabilir_mi(yol):
    return bool(yol) and os.path.isfile(yol) and os.access(yol, os.X_OK)


def _js_calisma_ortamlari():
    """yt-dlp 'js_runtimes' (YouTube JS challenge): bin/deno, then deno or node on PATH."""
    yerel = os.path.join(BOT_DIZINI, "bin", "deno")
    for ad, yol in (("deno", yerel if _calistirilabilir_mi(yerel) else shutil.which("deno")), ("node", shutil.which("node"))):
        if _calistirilabilir_mi(yol):
            return {ad: {"path": yol}}
    return {}


YTDLP_JS_CALISMA_ORTAMLARI = _js_calisma_ortamlari()
