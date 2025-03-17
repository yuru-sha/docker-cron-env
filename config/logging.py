"""
ロギング設定モジュール
"""

import logging


def get_logger(name: str = __name__) -> logging.Logger:
    """
    ロガーを取得する

    Args:
        name (str): ロガー名（デフォルト: 呼び出し元モジュール名）

    Returns:
        logging.Logger: 設定済みのロガーインスタンス
    """
    # 基本設定
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[logging.FileHandler("/var/log/cron.log"), logging.StreamHandler()],
    )

    # ロガーの取得
    return logging.getLogger(name)
