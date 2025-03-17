import logging
import sys

from config.settings import get_settings


def get_logger(
    name: str,
    log_level: int = None,
) -> logging.Logger:
    # .envファイルの読み込み
    settings = get_settings()

    log_level_str = settings.LOG_LEVEL
    log_level = getattr(logging, log_level_str.upper(), logging.INFO)

    # ロガーの設定
    logger = logging.getLogger(name)
    logger.setLevel(log_level)

    # 既存のハンドラを削除（重複を防ぐため）
    logger.handlers.clear()

    # フォーマッタの作成
    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # コンソールハンドラの設定
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger
