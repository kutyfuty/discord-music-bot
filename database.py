"""
Music bot database: one SQLite file (WAL). The music module creates its own tables (muzik_veritabani.py);
this file only adds the shared connection, per-server language and the admin check.
"""
import logging
import os
import sqlite3

from yapilandirma import DB_DOSYA, SAHIP_ID

logger = logging.getLogger('MusicBot.DB')

os.makedirs(os.path.dirname(DB_DOSYA), exist_ok=True)   # fresh clone: data/ does not exist yet
db = sqlite3.connect(DB_DOSYA, check_same_thread=False)
db.row_factory = sqlite3.Row
db.execute("PRAGMA journal_mode=WAL")
db.execute("PRAGMA synchronous=NORMAL")
db.execute("PRAGMA busy_timeout=5000")

_dil = {}   # {server_id: 'tr' | 'en'}


def veritabanini_kur():
    db.execute("CREATE TABLE IF NOT EXISTS sunucu_ayarlar (sunucu_id INTEGER PRIMARY KEY, dil TEXT DEFAULT 'tr')")
    db.commit()
    _dil.clear()
    _dil.update({r['sunucu_id']: r['dil'] for r in db.execute("SELECT sunucu_id, dil FROM sunucu_ayarlar")})


def sunucu_dil_al(sunucu_id):
    return _dil.get(sunucu_id) or 'tr'


def sunucu_dil_ayarla(sunucu_id, dil):
    kod = 'en' if str(dil).lower().startswith('en') else 'tr'
    db.execute("INSERT INTO sunucu_ayarlar (sunucu_id, dil) VALUES (?, ?) ON CONFLICT(sunucu_id) DO UPDATE SET dil = excluded.dil",
               (sunucu_id, kod))
    db.commit()
    _dil[sunucu_id] = kod
    return kod


def yonetici_mi(member):
    """Server admin: bot owner, or Administrator / Manage Server permission."""
    if SAHIP_ID and member.id == SAHIP_ID:
        return True
    izin = getattr(member, 'guild_permissions', None)
    return bool(izin is not None and (izin.administrator or izin.manage_guild))
