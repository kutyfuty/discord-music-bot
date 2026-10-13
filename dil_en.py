"""English translations — key: the Turkish _t(...) template in the code, exactly. tests/bot_test.py checks coverage."""

EN = {
    '**%{ses}**':
        '**{ses}%**',
    '{d0} dk {d2} sn':
        '{d0} min {d2} s',
    'Müzik':
        'Music',
    '{saniye} saniye':
        '{saniye} seconds',
    '{d0} dakika':
        '{d0} minutes',
    '{d0} saat':
        '{d0} hours',
    '{d0} gün':
        '{d0} days',
    '🎧 Bunu yapmak için benimle aynı ses kanalında (**{name}**) olmalısın.':
        '🎧 You need to be in the same voice channel as me (**{name}**) to do that.',
    '🎚️ Bu işlem için **DJ rolü** (<@&{rol_id}>) gerekli.':
        '🎚️ This needs the **DJ role** (<@&{rol_id}>).',
    '{bot} müzik paneli':
        '{bot} music panel',
    '⏹️ Durduruldu, kuyruk temizlendi. (7/24 modu: kanalda kalıyorum)':
        '⏹️ Stopped and cleared the queue. (24/7 mode: staying in the channel)',
    '⏹️ Durduruldu ve kanaldan ayrıldım.':
        '⏹️ Stopped and left the channel.',
    '❌ Önce bir ses kanalına gir!':
        '❌ Join a voice channel first!',
    '❌ **{name}** kanalına bağlanma/konuşma yetkim yok.':
        "❌ I don't have permission to connect or speak in **{name}**.",
    '❌ Ses bağlantısı zaman aşımına uğradı, tekrar dene.':
        '❌ Voice connection timed out, try again.',
    '❌ Sese bağlanılamadı: {e}':
        "❌ Couldn't connect to voice: {e}",
    '❌ Botun ses kütüphaneleri eksik (DAVE/davey). Bot sahibine haber ver.':
        "❌ The bot's voice libraries are missing (DAVE/davey). Let the bot owner know.",
    "🎧 Şu an **{name}** kanalında çalıyorum — oraya gel ya da DJ'e söyle.":
        "🎧 I'm playing in **{name}** right now — come there or ask a DJ.",
    '❌ Kanala taşınamadım: {e}':
        "❌ Couldn't move to the channel: {e}",
    'Spotify kısa linki çözülemedi':
        "couldn't resolve the Spotify short link",
    'Spotify kısa linki tanınmayan bir sayfaya gidiyor':
        'the Spotify short link leads to an unknown page',
    'sonuç bulunamadı':
        'no results found',
    'Spotify içeriği okunamadı (özel liste olabilir)':
        "couldn't read the Spotify content (it may be a private playlist)",
    'playlist boş ya da özel':
        'the playlist is empty or private',
    '❌ Kuyruk dolu ({limit} parça). Biraz çalınmasını bekle ya da `/temizle`.':
        '❌ The queue is full ({limit} tracks). Wait for some to play or use `/temizle`.',
    '❌ Çalınamıyor: {sebep}':
        "❌ Can't play: {sebep}",
    '📋 **{escape_markdown}** — **{eklenen}** parça {d5} eklendi.':
        '📋 **{escape_markdown}** — **{eklenen}** tracks added {d5}.',
    '⏳ Kalan parçalar arka planda ekleniyor… (toplam ~{toplam})':
        '⏳ Adding the remaining tracks in the background… (~{toplam} total)',
    '⚠️ Kuyruk sınırı ({limit}) nedeniyle {d3} parça eklenemedi.':
        "⚠️ {d3} tracks weren't added because of the queue limit ({limit}).",
    '▶️ **Şimdi çalınıyor**':
        '▶️ **Now playing**',
    '⏭️ **Sıradaki olarak eklendi**':
        '⏭️ **Added as next**',
    '✅ **Kuyruğa eklendi** · #{len}':
        '✅ **Added to the queue** · #{len}',
    "⚠️ Playlist'in kalanı yüklenemedi: {sebep}":
        "⚠️ Couldn't load the rest of the playlist: {sebep}",
    "📋 Playlist'in kalan **{eklenen}** parçası da kuyruğa eklendi.":
        '📋 The remaining **{eklenen}** tracks of the playlist were added to the queue too.',
    '❌ **{liste_adi}** listesi boş.':
        '❌ The **{liste_adi}** playlist is empty.',
    ' (⭐ Sunucu Listesi)':
        ' (⭐ Server Playlist)',
    ' (Paylaşılan)':
        ' (Shared)',
    'sıranın başına':
        'to the front of the queue',
    'kuyruğa':
        'to the queue',
    '📂 **{liste_adi}**{sahip_notu} — **{eklenen}** parça {yer_metni} eklendi.':
        '📂 **{liste_adi}**{sahip_notu} — **{eklenen}** tracks added {yer_metni}.',
    ' (Kuyruk sınırı: {d1} eklenemedi)':
        ' (Queue limit: {d1} not added)',
    '❌ Bir şarkı adı ya da link yaz: `/oynat tarkan şımarık`':
        '❌ Type a song name or link: `/oynat never gonna give you up`',
    '❌ Arama metni çok uzun!':
        '❌ The search text is too long!',
    '❌ Çalan bir şey yok.':
        '❌ Nothing is playing.',
    '🗳️ Oylama tamam ({n}/{gerekli}) — ⏭️ atlandı.':
        '🗳️ Vote passed ({n}/{gerekli}) — ⏭️ skipped.',
    '⏳ Geçiş sürüyor…':
        '⏳ Switching tracks…',
    "🗳️ Atlama oyu: **{len}/{gerekli}** — dinleyicilerin %{int}'i gerekli.":
        '🗳️ Skip votes: **{len}/{gerekli}** — {int}% of listeners needed.',
    'Bassboost: Kapalı':
        'Bassboost: Off',
    '🎶 Kuyruk boş.':
        '🎶 The queue is empty.',
    '❌ Şu an çalan bir şey yok. `/oynat` ile başla.':
        '❌ Nothing is playing right now. Start with `/oynat`.',
    '⏮️ Geçmişte önceki bir şarkı yok.':
        "⏮️ There's no previous song in the history.",
    '🔀 Karıştırmak için kuyrukta en az 2 parça olmalı.':
        '🔀 You need at least 2 tracks in the queue to shuffle.',
    '❤️ Bu şarkı zaten **Favoriler** listende.':
        '❤️ This song is already in your **Favorites** playlist.',
    '❌ Liste dolu ({LISTE_PARCA_LIMITI} parça).':
        '❌ The playlist is full ({LISTE_PARCA_LIMITI} tracks).',
    '❤️ **{gosterim}** → **Favoriler** listene eklendi. (`/calmalistesi oynat Favoriler`)':
        '❤️ **{gosterim}** → added to your **Favorites** playlist. (`/calmalistesi oynat Favoriler`)',
    '❌ Numara gir: `/atla 3` (sarmak için `/sar 1:30`)':
        '❌ Enter a number: `/atla 3` (to seek, use `/sar 1:30`)',
    '⏭️ {n}. parçaya atlandı.':
        '⏭️ Skipped to track {n}.',
    '⏳ Geçiş sürüyor, bir saniye…':
        '⏳ Switching tracks, one second…',
    '⏮️ **{gosterim}** tekrar çalıyor.':
        '⏮️ **{gosterim}** is playing again.',
    '⏸️ Duraklatıldı.':
        '⏸️ Paused.',
    '❌ Duraklatılmış bir şey yok.':
        '❌ Nothing is paused.',
    '▶️ Devam ediyor.':
        '▶️ Resumed.',
    '❌ Zaten çalan bir şey yok.':
        '❌ Nothing is playing.',
    '🔴 Canlı yayında sarılamaz.':
        "🔴 You can't seek in a live stream.",
    '❌ Geçersiz süre. Örnekler: `1:30`, `90`, `+30`, `-10`, `2m15s`':
        '❌ Invalid time. Examples: `1:30`, `90`, `+30`, `-10`, `2m15s`',
    '{ok} `{sure_metni}` konumuna sarıldı.':
        '{ok} Seeked to `{sure_metni}`.',
    '❌ Sarma başarısız oldu.':
        '❌ Seeking failed.',
    '🎶 Kuyruk boş. `/oynat` ile şarkı ekle.':
        '🎶 The queue is empty. Add songs with `/oynat`.',
    '❌ Kuyruk boş.':
        '❌ The queue is empty.',
    '❌ Geçersiz numara (1-{len}).':
        '❌ Invalid number (1-{len}).',
    ' (Kendi eklediğin parçaları kaldırabilirsin.)':
        ' (You can only remove tracks you added.)',
    '🗑️ **{gosterim}** kaldırıldı.':
        '🗑️ Removed **{gosterim}**.',
    '❌ Karıştırmak için kuyrukta en az 2 parça olmalı.':
        '❌ You need at least 2 tracks in the queue to shuffle.',
    '🔀 Kuyruk karıştırıldı!':
        '🔀 Queue shuffled!',
    '❌ Kuyruk zaten boş.':
        '❌ The queue is already empty.',
    '🧹 Kendi eklediğin **{n}** parça kaldırıldı.':
        '🧹 Removed **{n}** tracks you added.',
    '🧹 Kuyruk temizlendi ({n} parça).':
        '🧹 Queue cleared ({n} tracks).',
    '❌ Mod: `kapalı`, `şarkı` ya da `kuyruk`':
        '❌ Mode: `off`, `song` or `queue`',
    '{emoji} Döngü: **{DONGU_ETIKET}**':
        '{emoji} Loop: **{DONGU_ETIKET}**',
    '🔊 Ses: **%{mevcut}**  (değiştirmek: `/ses 80`, `/ses +10`)':
        '🔊 Volume: **{mevcut}%**  (to change: `/ses 80`, `/ses +10`)',
    '❌ 0-150 arası bir sayı gir.':
        '❌ Enter a number between 0 and 150.',
    '❌ Ses {SES_MIN}-{SES_MAX} arası olmalı.':
        '❌ Volume must be between {SES_MIN} and {SES_MAX}.',
    '{emoji} Ses **%{hedef}**':
        '{emoji} Volume **{hedef}%**',
    ' · 📢 %100 üstü sesi bozabilir':
        ' · 📢 above 100% may distort the sound',
    '🎶 Şu an bir şey çalmıyor.':
        '🎶 Nothing is playing right now.',
    '🎛️ Kontrol paneli bu kanala taşındı.':
        '🎛️ Control panel moved to this channel.',
    '🕘 Henüz bir şey çalınmadı.':
        '🕘 Nothing has been played yet.',
    '🎛️ Filtreler':
        '🎛️ Filters',
    '**Aktif:** {d1}\n\n':
        '**Active:** {d1}\n\n',
    'Kullanım: /filtre nightcore · /filtre bas 3 · /filtre hiz 1.25 · /filtre kapat':
        'Usage: /filtre nightcore · /filtre bas 3 · /filtre hiz 1.25 · /filtre kapat',
    '❌ Bilinmeyen filtre: `{secim}` — liste için `/filtre`':
        '❌ Unknown filter: `{secim}` — use `/filtre` for the list',
    '❌ Geçersiz değer.':
        '❌ Invalid value.',
    '\n-# Aktif: {join}':
        '\n-# Active: {join}',
    '❌ `aç` ya da `kapat` yaz.':
        '❌ Type `on` or `off`.',
    '📻 Otomatik oynatma: **{d1}**':
        '📻 Autoplay: **{d1}**',
    ' — kuyruk bitince benzer şarkılar çalacak.':
        ' — similar songs will play when the queue ends.',
    '✅ **{name}** kanalındayım. `/oynat` ile başla!':
        "✅ I'm in **{name}**. Start with `/oynat`!",
    '❌ Zaten bir ses kanalında değilim.':
        "❌ I'm not in a voice channel.",
    '👋 Görüşürüz!':
        '👋 See you!',
    '📂 Henüz kayıtlı liste yok. Çalan kuyruğu kaydet: `/calmalistesi kaydet <ad>` · ya da panelde ❤️ ile favorilere ekle.':
        '📂 No saved playlists yet. Save the current queue: `/calmalistesi kaydet <name>` · or add songs to favorites with ❤️ on the panel.',
    '📂 Çalma Listeleri':
        '📂 Playlists',
    '👤 **Kişisel Listelerin:**\n':
        '👤 **Your Playlists:**\n',
    '⭐ **Genel / Paylaşılan Listeler:**\n':
        '⭐ **Public / Shared Playlists:**\n',
    'Çal: /calmalistesi oynat <ad> · İçerik: /calmalistesi goster <ad>':
        'Play: /calmalistesi oynat <name> · Contents: /calmalistesi goster <name>',
    '❌ **{ad}** adında bir liste bulunamadı.':
        '❌ No playlist named **{ad}** was found.',
    ' (Sana ait)':
        ' (Yours)',
    '*Boş liste*':
        '*Empty playlist*',
    'Sayfa {d1}/{n} • {len} parça':
        'Page {d1}/{n} • {len} tracks',
    '❌ Kaydedilecek bir şey yok (çalan şarkı / kuyruk boş).':
        '❌ Nothing to save (no song playing and the queue is empty).',
    '💾 **{ad}** listesine **{n}** parça kaydedildi.':
        '💾 Saved **{n}** tracks to the **{ad}** playlist.',
    '❌ Çalan bir şey yok — eklemek için şarkı adı/link yaz.':
        '❌ Nothing is playing — type a song name or link to add.',
    '❌ Eklenemedi: {sebep}':
        "❌ Couldn't add: {sebep}",
    '➕ **{ad}** listesine {n} parça eklendi':
        '➕ Added {n} tracks to the **{ad}** playlist',
    '❌ **{ad}** adında sana ait bir liste yok.':
        "❌ You don't have a playlist named **{ad}**.",
    '🗑️ **{baslik}** listeden çıkarıldı.':
        '🗑️ Removed **{baslik}** from the playlist.',
    '❌ Geçersiz numara.':
        '❌ Invalid number.',
    '🗑️ **{ad}** listesi silindi.':
        '🗑️ Deleted the **{ad}** playlist.',
    '⚙️ Müzik Ayarları':
        '⚙️ Music Settings',
    '🎚️ DJ rolü':
        '🎚️ DJ role',
    'Kapalı (herkes kontrol eder)':
        'Off (everyone can control)',
    '🗳️ Oylamalı atla':
        '🗳️ Vote skip',
    ' (DJ rolü ayarlı → otomatik)':
        ' (DJ role set → automatic)',
    '🔊 Ses':
        '🔊 Volume',
    'Varsayılan %{a} · Son %{d3}':
        'Default {a}% · Last {d3}%',
    'Kapalı':
        'Off',
    '🌙 7/24 modu':
        '🌙 24/7 mode',
    'Açık':
        'On',
    '📻 Otomatik oynatma':
        '📻 Autoplay',
    '⏱️ Boşta ayrılma':
        '⏱️ Leave when idle',
    '📶 Normalizasyon':
        '📶 Normalization',
    '📨 İstek kanalı':
        '📨 Request channel',
    'Değiştir: /muzikayar dj · oylama · varsayilanses · surekli · otomatik · zamanasimi · istekkanali · normalizasyon':
        'Change: /muzikayar dj · oylama · varsayilanses · surekli · otomatik · zamanasimi · istekkanali · normalizasyon',
    '🚫 Bu ayar için sunucu yöneticisi (Yönetici / Sunucuyu Yönet)':
        '🚫 This setting needs a server admin (Administrator / Manage Server)',
    ' gerekli.':
        '.',
    ' ya da DJ rolü':
        ' or the DJ role',
    "🎚️ DJ rolü: {mention}. Artık kontrol komutları DJ'lere/yöneticilere özel, diğerleri oyla atlar.":
        '🎚️ DJ role: {mention}. Control commands are now limited to DJs/admins; everyone else votes to skip.',
    '🎚️ DJ sistemi kapatıldı — herkes kontrol edebilir.':
        '🎚️ DJ system turned off — everyone can control.',
    '❌ Oran %10-%100 arası olmalı.':
        '❌ The ratio must be between 10% and 100%.',
    "🗳️ Oylamalı atla açık — dinleyicilerin **%{sayi}**'i gerekli.":
        '🗳️ Vote skip is on — **{sayi}%** of listeners needed.',
    '❌ `aç`, `kapat` ya da bir yüzde yaz.':
        '❌ Type `on`, `off` or a percentage.',
    '🗳️ Oylamalı atla: **{d1}**':
        '🗳️ Vote skip: **{d1}**',
    ' (DJ rolü ayarlı olduğu için DJ olmayanlar yine oyla atlar)':
        ' (since a DJ role is set, non-DJs still vote to skip)',
    '🔊 Varsayılan ses **%{n}** (hatırlanan son ses sıfırlandı).':
        '🔊 Default volume **{n}%** (the remembered last volume was reset).',
    '🌙 7/24 modu: **{d1}**':
        '🌙 24/7 mode: **{d1}**',
    '📻 Otomatik oynatma (varsayılan): **{d1}**':
        '📻 Autoplay (default): **{d1}**',
    '❌ 30 saniye ile 60 dakika arası bir süre gir (ör. `3` = 3 dk, `90s`).':
        '❌ Enter a time between 30 seconds and 60 minutes (e.g. `3` = 3 min, `90s`).',
    '⏱️ Boşta/yalnız kalınca **{sure_metni}** sonra ayrılacağım (7/24 kapalıyken).':
        "⏱️ I'll leave after **{sure_metni}** of being idle/alone (when 24/7 is off).",
    '📶 Normalizasyon (varsayılan): **{d1}** — yeni oturumlarda geçerli; şu anki oturum için `/filtre normalizasyon`.':
        '📶 Normalization (default): **{d1}** — applies to new sessions; for the current session use `/filtre normalizasyon`.',
    '📨 Şarkı istek kanalı kapatıldı.':
        '📨 Song request channel turned off.',
    '❌ Kanal oluşturma yetkim yok — mevcut bir kanal belirt: `/muzikayar istekkanali #kanal`':
        "❌ I don't have permission to create channels — name an existing one: `/muzikayar istekkanali #channel`",
    '❌ {mention} kanalında **Mesaj Gönder, Bağlantı Yerleştir, Mesajları Yönet, Mesaj Geçmişini Oku** yetkilerim olmalı.':
        '❌ I need **Send Messages, Embed Links, Manage Messages, Read Message History** permissions in {mention}.',
    '📨 Şarkı istek kanalı: {mention} — oraya yazılan her mesaj aranıp kuyruğa eklenir, kontrol paneli de orada durur.':
        '📨 Song request channel: {mention} — every message there is searched and added to the queue, and the control panel stays there.',
    '⏳ yt-dlp güncelleniyor… (çalışan sürüm: `{calisan_surum}`)':
        '⏳ Updating yt-dlp… (running version: `{calisan_surum}`)',
    'sahip komutu':
        'owner command',
    '❌ Güncelleme başarısız:\n```{sonuc}```':
        '❌ Update failed:\n```{sonuc}```',
    '✅ yt-dlp zaten güncel: `{sonuc}`':
        '✅ yt-dlp is already up to date: `{sonuc}`',
    '✅ yt-dlp `{sonuc}` → `{sonuc2}`. ':
        '✅ yt-dlp `{sonuc}` → `{sonuc2}`. ',
    'Çalan müzikler bitince yeniden başlatacağım.':
        "I'll restart once the music currently playing ends.",
    'Yeniden başlatılıyor… 🔄':
        'Restarting… 🔄',
    'haftalık kontrol':
        'weekly check',
    '👋 Kanalda kimse kalmadı, ayrıldım. Tekrar görüşmek üzere!':
        "👋 Nobody's left in the channel, so I left. See you next time!",
    '💤 Bir süredir boştayım, kanaldan ayrıldım.':
        "💤 I've been idle for a while, so I left the channel.",
    '🔌 Ses bağlantısı koptu.':
        '🔌 The voice connection dropped.',
    '👋 Ses kanalından çıkarıldım.':
        '👋 I was removed from the voice channel.',
    '🔌 Ses bağlantısı koptu ve yeniden bağlanamadım.':
        "🔌 The voice connection dropped and I couldn't reconnect.",
    '🔌 Ses bağlantısı koptu — yeniden bağlandım, kaldığı yerden devam ediyorum.':
        "🔌 The voice connection dropped — I reconnected and I'm resuming where it left off.",
    '⏳ {mention} biraz yavaş — {ISTEK_BEKLEME:.0f} sn bekle.':
        '⏳ {mention}, slow down a little — wait {ISTEK_BEKLEME:.0f} s.',
    'Tüm efektler kapatıldı.':
        'All effects turned off.',
    'açık':
        'on',
    'kapalı':
        'off',
    'Hız: {deger:g}x':
        'Speed: {deger:g}x',
    'Normalizasyon: {durum}':
        'Normalization: {durum}',
    'pip {PIP_ZAMAN_ASIMI} sn içinde bitmedi':
        "pip didn't finish within {PIP_ZAMAN_ASIMI} s",
    'pip çalıştırılamadı: {e}':
        "couldn't run pip: {e}",
    'zaman aşımı':
        'timed out',
    'çözülemedi':
        "couldn't be resolved",
    'işçi süreci kapandı':
        'the worker process closed',
    'bilinmeyen hata':
        'unknown error',
    'çalınabilir ses formatı yok':
        'no playable audio format',
    'uygun sonuç bulunamadı':
        'no suitable result found',
    'Spotify sanatçı linkleri desteklenmiyor — şarkı, albüm ya da playlist linki gönder.':
        "Spotify artist links aren't supported — send a track, album or playlist link.",
    '⚠️ **{gosterim}** atlandı: {sebep}':
        '⚠️ Skipped **{gosterim}**: {sebep}',
    '❌ Üst üste çok fazla parça çözülemedi, oynatma durduruldu.':
        "❌ Too many tracks in a row couldn't be resolved, playback stopped.",
    '⚠️ **{gosterim}** akışı başlatılamadı, atlanıyor.':
        "⚠️ Couldn't start the stream for **{gosterim}**, skipping.",
    '⚠️ **{gosterim}** yeniden bağlanamadı: {sebep}':
        "⚠️ Couldn't reconnect **{gosterim}**: {sebep}",
    '⚠️ **{gosterim}** akışı koptu, sıradakine geçiliyor.':
        '⚠️ The stream for **{gosterim}** dropped, moving to the next one.',
    'Otomatik Oynatma':
        'Autoplay',
    '⚠️ Akış yenilenemedi: {sebep}':
        "⚠️ Couldn't refresh the stream: {sebep}",
    '⏸️ Duraklatıldı':
        '⏸️ Paused',
    '🔴 Canlı Yayın':
        '🔴 Live Stream',
    '🎶 Şu An Çalıyor':
        '🎶 Now Playing',
    '💤 *Kanalda kimse kalmadı — biri gelince kaldığı yerden devam edecek.*':
        "💤 *Nobody's left in the channel — it'll resume where it left off when someone joins.*",
    '📻 Otomatik':
        '📻 Autoplay',
    '👤 İsteyen':
        '👤 Requested by',
    '🔁 Döngü':
        '🔁 Loop',
    '📋 Kuyruk':
        '📋 Queue',
    '{len} parça':
        '{len} tracks',
    'Opus aktarım (kayıpsız)':
        'Opus pass-through (lossless)',
    'Opus · 160 kbps':
        'Opus · 160 kbps',
    '🎚️ Ses Yolu':
        '🎚️ Audio Path',
    '📶 Ses Dengeleme':
        '📶 Normalization',
    '🔂 Aynı şarkı tekrar çalacak':
        '🔂 The same song will play again',
    '\n-# … ve {d1} parça daha':
        '\n-# … and {d1} more tracks',
    '📻 Otomatik oynatma benzer bir parça bulacak':
        '📻 Autoplay will find a similar track',
    'Kuyruk boş — `/oynat` ile ekle':
        'The queue is empty — add songs with `/oynat`',
    '⏭️ Sıradaki':
        '⏭️ Up Next',
    '{bot} Premium Müzik':
        '{bot} Premium Music',
    '🎵 {bot} Müzik':
        '🎵 {bot} Music',
    '**Bir ses kanalına gir ve bu kanala şarkı adı ya da link yaz** — gerisini ben hallederim.\n-# Mesajın sıraya eklenince otomatik silinir; kanal hep temiz kalır.':
        "**Join a voice channel and type a song name or link in this channel** — I'll take care of the rest.\n-# Your message is deleted once it's queued, so the channel always stays clean.",
    'Bir ses kanalına gir ve `/oynat <şarkı>` ya da `{prefix}oynat <şarkı>` yaz.':
        'Join a voice channel and type `/oynat <song>` or `{prefix}play <song>`.',
    '{d0}Şu an bir şey çalmıyor.\n\n{nasil}':
        '{d0}Nothing is playing right now.\n\n{nasil}',
    '🌐 Kaynaklar':
        '🌐 Sources',
    '🔴 YouTube · 🎵 YouTube Music · 🟢 Spotify · 🟠 SoundCloud · 🔗 Doğrudan ses linki':
        '🔴 YouTube · 🎵 YouTube Music · 🟢 Spotify · 🟠 SoundCloud · 🔗 Direct audio link',
    '✨ Öne Çıkanlar':
        '✨ Highlights',
    '📻 Otomatik oynatma · 📶 Ses dengeleme · 🎤 Senkron sözler · ❤️ Kişisel listeler\n🛟 YouTube çalamazsa SoundCloud yedeği':
        '📻 Autoplay · 📶 Volume normalization · 🎤 Synced lyrics · ❤️ Personal playlists\n🛟 SoundCloud fallback when YouTube fails',
    '📜 Kuyruk':
        '📜 Queue',
    '**▶ Şimdi:** {parca_satiri}\n':
        '**▶ Now:** {parca_satiri}\n',
    '*Kuyruk boş.*':
        '*The queue is empty.*',
    ' 📻 Otomatik oynatma açık.':
        ' 📻 Autoplay is on.',
    'Sayfa {d1}/{sayfa_sayisi}  •  {len} parça':
        'Page {d1}/{sayfa_sayisi}  •  {len} tracks',
    '  •  Döngü: {get}':
        '  •  Loop: {get}',
    '🕘 Son Çalınanlar':
        '🕘 Recently Played',
    '*Henüz bir şey çalınmadı.*':
        '*Nothing has been played yet.*',
    '⏮️ önceki şarkıya dönmek için /onceki':
        '⏮️ use /onceki to go back to the previous song',
    '🎛️ Filtre / efekt seç…':
        '🎛️ Pick a filter / effect…',
    'Otomatik: Kapalı':
        'Autoplay: Off',
    'Favorilerime ekle':
        'Add to my favorites',
    'Otomatik: {d1}':
        'Autoplay: {d1}',
    '⚠️ Bir hata oluştu, tekrar dene.':
        '⚠️ Something went wrong, try again.',
    'Bu menü sana ait değil — kendi komutunu kullan.':
        "This menu isn't yours — use your own command.",
    '*♪ (giriş)*':
        '*♪ (intro)*',
    '*(boş)*':
        '*(empty)*',
    '✅ Sunucu dili **Türkçe** olarak ayarlandı. Bot bu sunucuda artık Türkçe yanıt verecektir.':
        '✅ Server language set to **English**. The bot will now reply in English on this server.',
    '⚠️ Eksik parametre: `{name}`. Kullanım için `{PREFIX}yardim` yaz.':
        '⚠️ Missing parameter: `{name}`. Type `{PREFIX}help` for usage.',
    '🚫 Bu komut sadece bot sahibine özel.':
        '🚫 This command is for the bot owner only.',
    '⚠️ Beklenmedik bir hata oluştu. Lütfen tekrar dene.':
        '⚠️ Something unexpected went wrong. Please try again.',
    '⏳ Yavaşla! Bu komut soğuma süresinde. **{kalan} saniye** sonra tekrar deneyebilirsin.':
        '⏳ Slow down! This command is on cooldown. You can try again in **{kalan} seconds**.',
    '🚫 Bu komutu kullanmak için yetkin yok (Yönetici yetkisi gereklidir).':
        "🚫 You don't have permission to use this command (Administrator is required).",
    '❌ Bu komut sadece sunucularda kullanılabilir.':
        '❌ This command can only be used in servers.',
    '⚠️ İşlem sırasında beklenmedik bir hata oluştu. Lütfen tekrar dene.':
        '⚠️ Something unexpected went wrong. Please try again.',
    'Liste adı boş olamaz.':
        "The playlist name can't be empty.",
    'En fazla {LISTE_LIMITI} kişisel listen olabilir.':
        'You can have at most {LISTE_LIMITI} personal playlists.',
    'parça':
        'track',
    'Spotify → YouTube':
        'Spotify → YouTube',
    'SoundCloud':
        'SoundCloud',
    'Filtresiz, saf ses':
        'No filters, pure sound',
    'Kuyruk':
        'Queue',
    'YouTube istek sınırı (geçici)':
        'YouTube rate limit (temporary)',
    'YouTube':
        'YouTube',
    'özel (gizli) video':
        'private video',
    'Ses dengeleme':
        'Volume normalization',
    'video kullanılamıyor / kaldırılmış':
        'video unavailable / removed',
    'DRM korumalı':
        'DRM protected',
    'YouTube bot doğrulaması istedi (geçici)':
        'YouTube asked for bot verification (temporary)',
    'Şarkılar arası ses farkını eşitler':
        'Evens out loudness between songs',
    'desteklenmeyen link':
        'unsupported link',
    'bölge engeli':
        'region blocked',
    'Doğrudan Link':
        'Direct Link',
    'telif nedeniyle kaldırılmış':
        'removed for copyright',
    'yayın henüz başlamadı':
        "the stream hasn't started yet",
    'çözücü süreci yeniden başlatıldı (geçici)':
        'the resolver process restarted (temporary)',
    'sadece kanal üyelerine açık':
        'members-only content',
    'Şarkı':
        'Song',
    'yaş kısıtlamalı (giriş gerekiyor)':
        'age-restricted (sign-in required)',
    'Efektleri kapat':
        'Turn off effects',
    'Şarkıyı atlar (oylama açıksa oy verir) · numara verirsen o parçaya atlar':
        'Skips the song (votes if voting is on) · give a number to jump to that track',
    'İsteğe bağlı: kuyruktaki şu numaralı parçaya atla':
        'Optional: jump to this track number in the queue',
    'Çalma listeleri (kişisel ve paylaşılan listeler)':
        'Playlists (personal and shared)',
    'Listenden bir parçayı çıkarır':
        'Remove a track from your playlist',
    'Parça numarası':
        'Track number',
    'Listene şarkı ekler (boş: çalan şarkı)':
        'Add a song to your playlist (empty: the current song)',
    'Şarkı adı / link (boş: çalan şarkı)':
        'Song name / link (empty: the current song)',
    'Liste adı (boş: tüm listeler)':
        'Playlist name (empty: all playlists)',
    'Çalan şarkı + kuyruğu kişisel listene kaydeder (aynı ad varsa üzerine yazar)':
        'Saves the current song + queue to your personal playlist (overwrites one with the same name)',
    'Liste adı':
        'Playlist name',
    'Çalma listesini kuyruğa ekler':
        'Adds a playlist to the queue',
    'Liste adı (varsayılan: Favoriler)':
        'Playlist name (default: Favoriler)',
    'Karıştırarak ekle (evet/hayır)':
        'Shuffle while adding (yes/no)',
    'Kişisel listeni tamamen siler':
        'Deletes your personal playlist entirely',
    'Botu ses kanalından çıkarır (kuyruk temizlenir)':
        'Disconnects the bot from voice (the queue is cleared)',
    'Duraklatılan müziği sürdürür':
        'Resumes paused music',
    '🇹🇷 Türkçe':
        '🇹🇷 Türkçe',
    '🇬🇧 English':
        '🇬🇧 English',
    'Döngü modu: kapalı / şarkı / kuyruk':
        'Loop mode: off / song / queue',
    'kapalı, şarkı ya da kuyruk (boş: sıradaki moda geç)':
        'off, song or queue (empty: switch to the next mode)',
    'Müziği duraklatır':
        'Pauses the music',
    'Çalmayı durdurur ve kuyruğu temizler (7/24 kapalıysa kanaldan ayrılır)':
        'Stops playback and clears the queue (leaves the channel if 24/7 is off)',
    'Şarkıyı geri sarar (varsayılan 10 sn)':
        'Rewinds the song (default 10 s)',
    'Şarkıyı ileri sarar (varsayılan 10 sn)':
        'Fast-forwards the song (default 10 s)',
    'Kaç saniye (ya da 1:00 gibi)':
        'How many seconds (or something like 1:00)',
    'Kuyruktan parça kaldırır':
        'Removes a track from the queue',
    'Kaldırılacak parçanın kuyruk numarası':
        'Queue number of the track to remove',
    'Kuyruğu karıştırır':
        'Shuffles the queue',
    'Botu ses kanalına çağırır':
        'Calls the bot to your voice channel',
    'Kuyruğu sayfa sayfa gösterir':
        'Shows the queue page by page',
    'Sunucunun müzik ayarları':
        "This server's music settings",
    "DJ rolünü ayarlar (boş: kapatır). DJ'ler kontrol komutlarını kullanır.":
        'Sets the DJ role (empty: turns it off). DJs use the control commands.',
    'DJ rolü (boş bırak = DJ sistemini kapat)':
        'DJ role (leave empty = turn off the DJ system)',
    'Şarkı istek kanalı: bu kanala yazılan her mesaj aranıp kuyruğa eklenir':
        'Song request channel: every message in this channel is searched and added to the queue',
    'Kanal (boş: yeni kanal oluştur)':
        'Channel (empty: create a new channel)',
    "'kapat' yazarsan istek kanalı kapatılır":
        "Type 'kapat' to turn the request channel off",
    'Ses normalizasyonunun varsayılan durumu':
        'Default state of volume normalization',
    'Otomatik oynatmanın varsayılan durumu':
        'Default state of autoplay',
    'Oylamalı atla: aç / kapat ya da gereken oran (ör. 60)':
        'Vote skip: on / off or the required ratio (e.g. 60)',
    'aç, kapat ya da yüzde (10-100)':
        'on, off or a percentage (10-100)',
    '7/24 modu: boşta/yalnızken kanaldan ayrılma':
        "24/7 mode: don't leave the channel when idle/alone",
    'aç / kapat':
        'on / off',
    'Yeni oturumların başlangıç sesi (0-150)':
        'Starting volume for new sessions (0-150)',
    '0-150':
        '0-150',
    'Boşta ya da kanalda yalnız kalınca kaç dakika sonra ayrılsın':
        'How many minutes to wait before leaving when idle or alone',
    'Dakika (ör. 3) ya da 90s, 1:30 (30 sn – 60 dk)':
        'Minutes (e.g. 3) or 90s, 1:30 (30 s – 60 min)',
    'Bu sunucuda son çalınan şarkılar':
        'Songs played recently on this server',
    'Ses dengeleme (şarkılar arası ses farkını eşitler) aç/kapat':
        'Volume normalization (evens out loudness between songs) on/off',
    'Önceki şarkıya döner':
        'Goes back to the previous song',
    'Otomatik oynatma: kuyruk bitince benzer şarkılarla devam eder':
        'Autoplay: keeps going with similar songs when the queue ends',
    'aç / kapat (boş: değiştir)':
        'on / off (empty: toggle)',
    'Oylamalı atlamayı açar/kapatır ya da gereken oranı ayarlar':
        'Turns vote skip on/off or sets the required ratio',
    'aç / kapat ya da gereken oran (ör. 60)':
        'on / off or the required ratio (e.g. 60)',
    'Şarkıyı atlamak için oy verir':
        'Votes to skip the song',
    'Şarkı / playlist çalar (YouTube, YT Music, Spotify, SoundCloud, link)':
        'Plays a song / playlist (YouTube, YT Music, Spotify, SoundCloud, link)',
    'Şarkı adı ya da link (YouTube, YT Music, Spotify, SoundCloud, doğrudan ses linki)':
        'Song name or link (YouTube, YT Music, Spotify, SoundCloud, direct audio link)',
    'Şarkıda belirli bir ana sarar (1:30, +30, -10)':
        'Seeks to a specific point in the song (1:30, +30, -10)',
    'Örnek: 1:30 (mutlak), +30 (ileri), -10 (geri)':
        'Example: 1:30 (absolute), +30 (forward), -10 (back)',
    'Ses seviyesi (0-150, sunucuya özel hatırlanır)':
        'Volume level (0-150, remembered per server)',
    '0-150 arası, ya da +10 / -10':
        '0-150, or +10 / -10',
    'Şu an çalanı ve kontrol panelini gösterir (paneli bu kanala taşır)':
        "Shows what's playing and the control panel (moves the panel to this channel)",
    'Şarkıyı kuyruğun en başına ekler (sıradaki çalar)':
        'Adds a song to the front of the queue (plays next)',
    'Şarkı adı ya da link':
        'Song name or link',
    'Kuyrukta parçanın yerini değiştirir':
        'Moves a track to another position in the queue',
    'Taşınacak parçanın numarası':
        'Number of the track to move',
    'Yeni konumu':
        'Its new position',
    'Kuyruğu temizler (DJ değilsen sadece kendi eklediklerini)':
        "Clears the queue (if you're not a DJ, only the tracks you added)",
    "[Bot Sahibi] yt-dlp'yi venv'de günceller":
        '[Bot Owner] Updates yt-dlp in the venv',
    'bekle: çalan şarkılar bitince yeniden başlat':
        'bekle: restart once the playing songs end',
    "🎧 Senin odanda **{bot}** çalıyor. Komutu ondan kullan: `/{komut}` yazınca listeden **{bot}**'u seç (ya da `!{komut}` yaz).":
        '🎧 **{bot}** is playing in your channel. Use its command instead: type `/{komut}` and pick **{bot}** from the list (or type `!{komut}`).',
    "🎶 Ben şu an **{kanal}** kanalında çalıyorum. Senin odan için **{bot}** boşta: `/{komut}` yazıp listeden **{bot}**'u seç (ya da `!{komut}` yaz, boştaki bot kendisi gelir).":
        "🎶 I'm playing in **{kanal}** right now. **{bot}** is free for your channel: type `/{komut}` and pick **{bot}** (or type `!{komut}` and the free bot joins by itself).",
    '🎶 {bot} — müzik komutları':
        '🎶 {bot} — music commands',
    '🎵 Çalma':
        '🎵 Playback',
    '🎚️ Ses':
        '🎚️ Sound',
    '💾 Listeler ve ayarlar':
        '💾 Playlists and settings',
    'YouTube, YouTube Music, Spotify, SoundCloud ya da doğrudan link çalar':
        'Plays YouTube, YouTube Music, Spotify, SoundCloud or a direct link',
    'Şarkıyı kuyruğun başına ekler':
        'Adds a song to the front of the queue',
    'Sonraki / önceki şarkı, oylamalı atlama':
        'Next / previous song, vote skip',
    'Duraklat, sürdür, durdur ve kuyruğu temizle':
        'Pause, resume, stop and clear the queue',
    'Şarkıda ileri / geri sar':
        'Seek forward / back',
    'Kuyruğu ve çalan şarkıyı gösterir':
        'Shows the queue and the current song',
    'Kuyruğu düzenle':
        'Edit the queue',
    'Tekrar modu ve otomatik oynatma (radyo)':
        'Loop mode and autoplay (radio)',
    'Ses seviyesi ve ses dengeleme':
        'Volume and loudness normalization',
    'Odaya çağır / odadan çıkar':
        'Join / leave the voice channel',
    'Kişisel çalma listelerin (kaydet, ekle, oynat, sil)':
        'Your personal playlists (save, add, play, delete)',
    'DJ rolü, 7/24 modu, istek kanalı, zaman aşımı (yönetici)':
        'DJ role, 24/7 mode, request channel, idle timeout (admins)',
    'Botun bu sunucudaki dili (yönetici)':
        "The bot's language in this server (admins)",
    '🎧 Birden çok müzik botu':
        '🎧 Several music bots',
    'Bu sunucuda birden çok müzik botu var: `{prefix}oynat` yazınca **senin** ses kanalındaki bot cevap verir, odanda bot yoksa boştaki gelir.':
        'This server has several music bots: type `{prefix}oynat` and the bot in **your** voice channel answers; if your channel has none, a free bot joins.',
}
