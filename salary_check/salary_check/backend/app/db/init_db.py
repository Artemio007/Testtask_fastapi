import asyncio
import hashlib
import logging

from fastapi_users.exceptions import FastAPIUsersException
from pydantic import ValidationError
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.user import UserCreate
from app.core.confiig import Settings
from app.crud.user import create_init_user

settings = Settings()
logger = logging.getLogger('bank_aggregator')


def init_db(adb: AsyncSession):
    asyncio.run(create_user(adb))


async def create_user(db: AsyncSession) -> None:
    try:
        users = settings.INIT_USER
        for user in users:
            db_user = UserCreate(
                user_name=hashlib.sha256(user["user_name"].encode()).hexdigest(),
                user_middle_name=user["user_middle_name"],
                user_last_name=user["user_last_name"],
                email=user["email"],
                password=user["password"],
                is_superuser=user["is_superuser"],
            )
            create_init_user(db, db_user)

    except ValidationError as err:
        logger.error(f"You have some err in func 'create_user': {err}")
    except FastAPIUsersException as err:
        logger.info(f"have an error in init db create_user {err}")
    except Exception as err:
        logger.info(f"have an error in init db create_user {err}")
    else:
        async with db.begin():
            await create_init_user(db, db_user)
