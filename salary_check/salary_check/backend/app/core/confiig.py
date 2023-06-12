import os
from pathlib import Path
from pydantic import BaseSettings

BASE_DIR = (Path(__file__) / ".." / ".." / ".." / "..").resolve()
ENV_PATH = os.path.join(BASE_DIR, ".env")


class Settings(BaseSettings):
    PROJECT_NAME: str
    PROJECT_VERSION: str
    PROJECT_HOST: str
    PROJECT_PORT: int

    POSTGRES_USER: str
    POSTGRES_DB: str
    POSTGRES_PASSWORD: str
    DB_HOST: str
    DB_PORT: int

    SECRET: str

    INIT_USER: tuple = [{
        "user_name": "Artem",
        "user_middle_name": "Viyalievich",
        "user_last_name": "Mozalev",
        "email": "mvamvh@gmail.com",
        "password": "s4gF3dsg45D#$",
        "is_superuser": True,
    },
        {"user_name": "Ivan",
         "user_middle_name": "Ivanovich",
         "user_last_name": "Ivanov",
         "email": "ivanov@gmail.com",
         "password": "s4gF3dsg45hj2D#$",
         "is_superuser": False,
         }]

    class Config:
        env_file = ENV_PATH
        env_file_encoding = "utf-8"
        case_sensitive = True


settings = Settings()

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "%(levelname)-7s %(asctime)s %(message)s"
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "standard"
        },
        "file": {
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": os.path.join(BASE_DIR, 'logs', 'api.log'),
            "formatter": "standard",
            "encoding": "UTF-8",
            "maxBytes": 10 * 1024 * 1024,
            "backupCount": 1000
        }
    },
    "loggers": {
        "salary_check": {
            "handlers": ["console", "file"],
            "level": "DEBUG"
        }
    }
}
