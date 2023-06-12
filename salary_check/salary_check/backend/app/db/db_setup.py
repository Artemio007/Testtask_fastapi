from app.core.confiig import settings

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine


SQLALCHEMY_DATABASE_URL = f'postgresql+asyncpg://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@' \
                          f'db_app_postgres:{settings.DB_PORT}/{settings.POSTGRES_DB}'


engine = create_async_engine(SQLALCHEMY_DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)
