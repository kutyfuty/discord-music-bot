# Discord music bot — Docker image
FROM denoland/deno:bin AS deno

FROM python:3.14-slim
ENV PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1 \
    HOME=/app/data XDG_CACHE_HOME=/app/data/.cache TMPDIR=/app/data/tmp
# FFmpeg (audio), Deno (yt-dlp's YouTube JS challenge solver)
RUN apt-get update && apt-get install -y --no-install-recommends ffmpeg ca-certificates \
    && rm -rf /var/lib/apt/lists/*
COPY --from=deno /deno /usr/local/bin/deno

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN useradd --uid 1000 --home /app/data musicbot \
    && mkdir -p /app/data/tmp && chown -R musicbot /app
USER musicbot
CMD ["python", "main.py"]
