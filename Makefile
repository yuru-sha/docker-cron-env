.PHONY: help build up down logs ps clean lint lint-fix format

# デフォルトのターゲット
.DEFAULT_GOAL := help

# 環境変数ファイルの存在確認
ENV_FILE := .env
$(ENV_FILE):
	@echo "環境変数ファイルをコピーします..."
	@cp .env.example $(ENV_FILE)

# ヘルプ
help:
	@echo "利用可能なコマンド:"
	@echo "  make setup     - 初期セットアップを実行（.envファイルの作成、依存関係のインストール）"
	@echo "  make build    - Dockerイメージをビルド"
	@echo "  make up       - コンテナを起動"
	@echo "  make down     - コンテナを停止"
	@echo "  make logs     - コンテナのログを表示"
	@echo "  make ps       - 実行中のコンテナを表示"
	@echo "  make clean    - 未使用のDockerリソースを削除"
	@echo "  make lint     - ruffでコードをチェック"
	@echo "  make lint-fix - ruffでコードをチェックして自動修正"
	@echo "  make format   - ruffでコードを自動フォーマット"
	@echo "  make help     - このヘルプメッセージを表示"

# 初期セットアップ
setup: $(ENV_FILE)
	@echo "依存関係をインストールしています..."
	@python -m pip install -r requirements.txt
	@echo "セットアップが完了しました。"

# Dockerイメージのビルド
build:
	docker compose build

# コンテナの起動
up:
	@mkdir -p logs
	docker compose up -d

# コンテナの停止
down:
	docker compose down

# ログの表示
logs:
	docker compose logs -f

# コンテナの状態確認
ps:
	docker compose ps

# コードのlint（チェックのみ）
lint:
	@echo "Pythonコードをチェックしています..."
	uv run ruff check --statistics .

# コードのフォーマット
format:
	@echo "Pythonコードをフォーマットしています..."
	uv run ruff format .
	uv run ruff check --fix .

# クリーンアップ
clean:
	docker compose down -v --remove-orphans
	rm -rf logs/*
	@echo "未使用のDockerイメージを削除します..."
	-docker image prune -f
	@echo "未使用のDockerボリュームを削除します..."
	-docker volume prune -f
	@echo "クリーンアップが完了しました。"
