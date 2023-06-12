import hashlib
import logging
import string
import secrets
import datetime


from fastapi_users.db import SQLAlchemyUserDatabase
from fastapi_users.exceptions import FastAPIUsersException
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import User
from app.db.session import get_async_session


logger = logging.getLogger('salary_check')


async def create_init_user(db: AsyncSession, user: User) -> User:
    try:

        db_user = User(
            user_name=user.user_name,
            user_middle_name=user.user_middle_name,
            user_last_name=user.user_last_name,
            email=user.email,
            password=user.password,
            is_superuser=user.is_superuser,
        )
        db.add(db_user)
        await db.commit()
        logger.info(f'Created user db {db_user}')
        return db_user
    except FastAPIUsersException as err:
        logger.info(f"Have an error in crud/create_init_user - {err}")
    except Exception as err:
        logger.info(f"Have an error in crud/create_init_user - {err}")


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)


async def generate_token(length: int = 10) -> str:
    alphabet = string.ascii_letters + string.digits
    token = ''.join(secrets.choice(alphabet) for _ in range(length))
    return token


async def add_secret_token(db: get_async_session, user_id: int) -> None:
    try:
        token = await generate_token()
        hashed_key = hashlib.sha256(token.encode()).hexdigest()
        token_live_time = datetime.datetime.utcnow()

        async with db as session:
            user = await session.get(User, user_id)
            if user:
                user.hashed_token = hashed_key
                user.token_live_time = token_live_time
                await session.commit()
                logger.info("Secret token added successfully")
            else:
                logger.info("User not found")
        return token
    except Exception as err:
        logger.info(f"Error in adding secret token: {err}")


