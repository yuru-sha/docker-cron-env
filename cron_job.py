import os
from datetime import datetime

from dotenv import load_dotenv

from config.logging import get_logger

# ロガーの取得
logger = get_logger(__name__)


def main():
    try:
        # .envファイルの読み込み
        load_dotenv()

        # 環境変数の取得
        message = os.getenv("CRON_MESSAGE", "デフォルトメッセージ")

        # 現在時刻を取得
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # ログ出力
        logger.info(f"Cronジョブ実行時刻: {current_time}")
        logger.info(f"メッセージ: {message}")
    except Exception as e:
        logger.error(f"エラーが発生しました: {str(e)}", exc_info=True)
        raise


if __name__ == "__main__":
    main()
