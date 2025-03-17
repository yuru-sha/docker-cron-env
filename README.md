# Docker Cron Environment

Python 3.12とcronを使用した環境変数対応のDockerコンテナサンプルです。

## 特徴

- Python 3.12
- python-dotenvによる環境変数の管理
- uvによるパッケージ管理
- 2フェーズビルドのDockerfile
- ログ出力機能
- Docker Compose対応

## 前提条件

- Docker
- Docker Compose v2

## 使用方法

### Docker Composeを使用する場合（推奨）

1. 環境変数ファイルの準備:
```bash
cp .env.example .env
```

2. コンテナの起動:
```bash
docker compose up -d --build
```

3. ログの確認:
```bash
# ホストマシンの logs ディレクトリに直接出力されます
tail -f logs/cron.log
```

### Docker単体を使用する場合

1. 環境変数ファイルの準備:
```bash
cp .env.example .env
```

2. Dockerイメージのビルド:
```bash
docker build -t cron-env -f docker/Dockerfile .
```

3. コンテナの実行:
```bash
docker run -d \
  --name cron-container \
  -v "$(pwd)/.env:/app/.env:ro" \
  -v "$(pwd)/logs:/var/log" \
  cron-env
```

4. ログの確認:
```bash
tail -f logs/cron.log
```

### コンテナの停止と削除

```bash
# Docker Composeの場合
docker compose down

# Docker単体の場合
docker stop cron-container
docker rm cron-container
```

## 環境変数

- `CRON_MESSAGE`: cronジョブで表示されるメッセージ（デフォルト: "デフォルトメッセージ"）

## トラブルシューティング

### ログが出力されない場合

1. コンテナが正常に動作していることを確認:
```bash
docker ps
```

2. cronデーモンの状態を確認:
```bash
docker exec cron-container service cron status
```

3. crontabの設定を確認:
```bash
docker exec cron-container crontab -l
```

## ディレクトリ構造

```
.
├── docker/
│   ├── Dockerfile     # マルチステージビルド用Dockerfile
│   ├── crontab        # cronジョブの設定ファイル
│   └── entrypoint.sh  # コンテナ起動時の初期化スクリプト
├── logs/              # ログ出力ディレクトリ
├── cron_job.py        # 実行されるPythonスクリプト
├── docker-compose.yml # Docker Compose設定ファイル
├── requirements.txt   # Pythonパッケージの依存関係
├── .env.example       # 環境変数のサンプルファイル
└── README.md         # このファイル
```

## 注意事項

- ログディレクトリ（`logs/`）は自動的に作成されます
- 環境変数ファイル（`.env`）は必ず準備してください
- コンテナは`unless-stopped`設定で自動再起動します