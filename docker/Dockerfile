# ビルドステージ
FROM python:3.12-slim AS builder

WORKDIR /app

# 必要なパッケージのインストール
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    build-essential \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# uv のインストール
RUN pip install uv

# 依存関係のインストール
COPY requirements.txt .
RUN pip install -r requirements.txt

# 実行ステージ
FROM python:3.12-slim

WORKDIR /app

# cronのインストール
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    cron \
    tzdata \
    && rm -rf /var/lib/apt/lists/*

# ビルドステージから依存関係をコピー
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# アプリケーションファイルのコピー
COPY docker-cron-env/ docker-cron-env/
COPY docker/crontab /etc/cron.d/app-cron
COPY docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# crontabの権限設定
RUN chmod 0644 /etc/cron.d/app-cron && \
    crontab /etc/cron.d/app-cron && \
    touch /var/log/cron.log && \
    chmod 0666 /var/log/cron.log

# タイムゾーンの設定
ENV TZ=Asia/Tokyo
RUN ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime

# エントリーポイントの設定
ENTRYPOINT ["/entrypoint.sh"]