from config.logging import get_logger
from config.settings import get_settings

settings = get_settings()
logger = get_logger(__name__)


def main():
    try:
        cron_message = settings.CRON_MESSAGE
        logger.info(f"メッセージ: {cron_message}")
    except Exception as e:
        logger.error(f"An eror occurred: {str(e)}", exec_info=True)
        raise


if __name__ == "__main__":
    main()
