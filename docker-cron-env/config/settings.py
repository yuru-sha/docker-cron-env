from dotenv import load_dotenv
from pydantic import Field, field_validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    LOG_LEVEL: str | None = Field(default="DEBUG")
    CRON_MESSAGE: str | None = Field(default=None)

    @field_validator("LOG_LEVEL")
    def validate_log_level(cls, v):
        if v not in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]:
            raise ValueError(
                "LOG_LEVEL must be one of DEBUG, INFO, WARNING, ERROR, or CRITICAL"
            )
        return v

    @field_validator("CRON_MESSAGE")
    def validate_cron_message(cls, v):
        if v is None:
            raise ValueError("CRON_MESSAGE must be provided")
        return v


def get_settings() -> Settings:
    # .envファイルの読み込み
    load_dotenv(verbose=True)
    return Settings()
