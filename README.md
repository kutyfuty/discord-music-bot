# 🎶 Discord Music Bot

A self-hosted, music-only Discord bot. No moderation, no economy — just music that doesn't stutter.
It is the music engine of [MezarBot](https://github.com/kutyfuty/mezarbot), published on its own.

**English** · [Türkçe](#-türkçe)

## ✨ Features

- **Sources:** YouTube, YouTube Music, Spotify (tracks, albums, playlists), SoundCloud and direct audio links
- **SoundCloud fallback:** if YouTube refuses a song (bot check, age or region lock, removed video), the same song is
  found on SoundCloud — 30-second previews and covers/remixes are skipped
- **Panel:** a persistent now-playing panel with buttons, a progress bar and live synced lyrics
- **Queue:** loop, shuffle, move, remove, seek, vote skip, previous song, autoplay (radio), 24/7 mode
- **Sound:** volume 0–150, loudness normalization, filters (bass, nightcore, 8D …), lossless Opus pass-through
- **Server tools:** DJ role, song request channel (type a song name, it gets queued), idle timeout
- **Personal playlists** and play history
- **Two voice channels at once** with a second bot account (see below)
- Turkish and English (`/dil en`), `!` prefix and `/` slash commands, DAVE end-to-end voice encryption

## 🚀 Setup

Requirements: Python 3.11+, FFmpeg, and [Deno](https://deno.com) (or Node.js) for YouTube's JS challenge.

```bash
git clone https://github.com/kutyfuty/discord-music-bot && cd discord-music-bot
python -m venv venv && venv/bin/pip install -r requirements.txt
cp .env.example .env              # put DISCORD_TOKEN in it
cp config.example.json config.json
venv/bin/python main.py
```

In the [Developer Portal](https://discord.com/developers/applications) → your app → **Bot**, turn on
**Server Members Intent** and **Message Content Intent**. Invite link (scopes `bot applications.commands`,
permissions: view channels, send messages, manage messages, embed links, read history, connect, speak):

```
https://discord.com/oauth2/authorize?client_id=YOUR_APP_ID&scope=bot+applications.commands&permissions=4332055616
```

Docker: `docker compose up -d`

## 🎧 Two rooms at once

A Discord bot account can only be in **one** voice channel per server. For a second room, create a second bot
application and run this code twice:

1. Put the second token in `.env.2` (`DISCORD_TOKEN=...`).
2. In `config.json` list both bot IDs in priority order: `"music_instances": ["<bot 1 id>", "<bot 2 id>"]`.
3. Run `BOT_INSTANCE=2 venv/bin/python main.py` next to the first one (or `docker compose --profile two up -d`).

Commands are smart: when you type `!oynat`, only the bot in **your** voice channel answers. If your channel has no
bot, the first free bot joins; the others stay silent. If you pick the wrong bot in the slash menu, it tells you which
bot plays in your channel. The bots never talk to each other: each reads Discord's voice states and reaches the
same decision. Each instance keeps its own lock, log and database, and only the first one updates yt-dlp.

## 🧪 Tests

```bash
venv/bin/python tests/bot_test.py            # cogs load, translations, second instance, which bot answers
venv/bin/python tests/muzik_test.py --agsiz  # music engine, offline (drop the flag to test real streams)
```

## 📄 License

MIT

---

## 🇹🇷 Türkçe

Kendi sunucunda çalışan, **yalnızca müzik** çalan Discord botu. Moderasyon ya da ekonomi yok, sadece takılmayan müzik.
[MezarBot](https://github.com/kutyfuty/mezarbot)'un müzik motorunun ayrı yayınlanmış hâli.

### ✨ Özellikler

- **Kaynaklar:** YouTube, YouTube Music, Spotify (şarkı, albüm, liste), SoundCloud ve doğrudan ses linkleri
- **SoundCloud yedeği:** YouTube bir şarkıyı çalmazsa (bot doğrulaması, yaş/bölge kısıtı, kaldırılmış video) aynı şarkı
  SoundCloud'da bulunur; 30 sn'lik önizlemeler ve cover/remix gibi yanlış eşleşmeler atlanır
- **Panel:** butonlu kalıcı "şu an çalıyor" paneli, ilerleme çubuğu, canlı akan senkron sözler
- **Kuyruk:** döngü, karıştır, taşı, kaldır, sar, oylamalı atla, önceki şarkı, otomatik oynatma (radyo), 7/24 modu
- **Ses:** 0–150 ses, ses dengeleme, filtreler (bas, nightcore, 8D …), kayıpsız Opus aktarımı
- **Sunucu araçları:** DJ rolü, şarkı istek kanalı (şarkı adını yaz, kuyruğa eklenir), boşta kalınca ayrılma süresi
- **Kişisel çalma listeleri** ve çalma geçmişi
- İkinci bot hesabıyla **iki odada aynı anda** müzik
- Türkçe ve İngilizce (`/dil en`), `!` önekli ve `/` slash komutları, DAVE uçtan uca ses şifreleme

### 🚀 Kurulum

Gerekenler: Python 3.11+, FFmpeg ve YouTube'un JS doğrulaması için [Deno](https://deno.com) (ya da Node.js).

```bash
git clone https://github.com/kutyfuty/discord-music-bot && cd discord-music-bot
python -m venv venv && venv/bin/pip install -r requirements.txt
cp .env.example .env              # DISCORD_TOKEN'ı yaz
cp config.example.json config.json
venv/bin/python main.py
```

[Developer Portal](https://discord.com/developers/applications) → uygulaman → **Bot** bölümünde **Server Members Intent**
ve **Message Content Intent** açık olmalı. Davet linkindeki `YOUR_APP_ID` yerine uygulamanın ID'sini yaz (yukarıda).
Docker: `docker compose up -d`

### 🎧 İki odada aynı anda

Bir Discord bot hesabı bir sunucuda aynı anda **tek** ses kanalında olabilir. İkinci oda için ikinci bir bot uygulaması
oluştur ve bu kodu iki kez çalıştır:

1. İkinci token'ı `.env.2` dosyasına yaz (`DISCORD_TOKEN=...`).
2. `config.json` → `"music_instances": ["<1. bot id>", "<2. bot id>"]` (sıra = öncelik).
3. İlkinin yanında `BOT_INSTANCE=2 venv/bin/python main.py` çalıştır (ya da `docker compose --profile two up -d`).

Komutlar akıllıdır: `!oynat` yazınca yalnızca **senin** ses kanalındaki bot cevap verir; odanda bot yoksa boştaki ilk bot
gelir, diğerleri susar. Slash menüsünde yanlış botu seçersen odanda hangi botun çaldığını söyler. Botlar birbiriyle
konuşmaz; her biri Discord'un ses durumlarına bakıp aynı kararı verir. Her birinin kendi kilidi, log'u ve veritabanı
vardır; yt-dlp'yi yalnızca ilki günceller.

### 🧪 Testler

```bash
venv/bin/python tests/bot_test.py            # cog'lar, çeviriler, ikinci bot, hangi bot cevap verir
venv/bin/python tests/muzik_test.py --agsiz  # müzik motoru, ağsız (parametresiz: gerçek akış testleri de)
```

### 📄 Lisans

MIT
