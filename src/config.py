from typing import Any

from pydantic import BaseSettings, PostgresDsn, root_validator
from src.constants import Enviroment
from dotenv import load_dotenv

load_dotenv()

class Config(BaseSettings):
    DATABASE_URL: PostgresDsn

    SITE_DOMAIN: str = "backend.tsuchigomori.dev"

    ENVIROMENT: Enviroment = Enviroment.PRODUCTION

    SENTRY_DNS: str | None

    CORS_ORIGINS: list[str]
    CORS_ORIGINS_REGEX: str | None
    CORS_HEADERS: list[str]

    APP_VERSION: str = "1"

    @root_validator(skip_on_failure=True)
    def validate_sentry_non_local(cls, data: dict[str, Any]) -> dict[str, Any]:
        if data["ENVIRONMENT"].is_deployed and not data["SENTRY_DSN"]:
            raise ValueError("Sentry is not set")

        return data

settings = Config()

app_configs: dict[str, Any] = {"title": "App API"}
if settings.ENVIRONMENT.is_deployed:
    app_configs["root_path"] = f"/v{settings.APP_VERSION}"

if not settings.ENVIRONMENT.is_debug:
    app_configs["openapi_url"] = None  # hide docs