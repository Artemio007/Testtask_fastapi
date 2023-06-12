import datetime
import hashlib

from fastapi import FastAPI, Depends, HTTPException
import logging

from sqlalchemy import select

from app.api.api import api_router, fastapi_users
from app.models.user import User

from app.crud.salary import create_salary_size_data
from app.db.session import get_async_session
from app.crud.user import add_secret_token
from app.models.salary_data import SalaryData
from sqlalchemy.ext.asyncio import AsyncSession

logging.basicConfig(level=logging.INFO, filename="fastlog.log", filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger('salary_check')

app = FastAPI()
app.include_router(api_router)
current_user = fastapi_users.current_user()


@app.post("/create_token")
async def create_token(user: User = Depends(current_user), db: get_async_session = Depends(get_async_session)):
    try:
        hashed_token = await add_secret_token(db, user.id)
        logger.info(f"{user.email} получил секретный ключ")
        return f"Привет, {user.email}, вот твой секретный ключ - {hashed_token}. Используй его для проверки зарплаты."
    except Exception as err:
        logger.info(f"ошибка в функции protected_route {err}")
        return "Произошла ошибка. Пожалуйста, попробуйте еще раз."


@app.post("/salary-data_for_superuser")
async def add_salary_data(salary_size: float, user_id: int, db=Depends(get_async_session),
                          user: User = Depends(current_user)):
    if user.is_superuser:
        try:
            await create_salary_size_data(db, user_id, salary_size)
            logger.info(f"{user.email} изменил данные в таблице salarydata")
            return f"{user.email}, данные изменены успешно"
        except Exception as err:
            return f"Возникла ошибка {err}"
    else:
        logger.info(f"Попытка изменения данных: {user.email}")
        return f"{user.email}, вы не суперюзер"


@app.get("/get_salary_by_token")
async def get_salary_by_token(token: str, user: User = Depends(current_user),
                            db: AsyncSession = Depends(get_async_session)):
    try:
        if not user.is_active:
            raise HTTPException(status_code=401, detail="Пользователь не авторизован")

        hashed_input_token = hashlib.sha256(token.encode()).hexdigest()
        query = select(User).where(User.hashed_token == hashed_input_token)
        result = await db.execute(query)
        user = result.scalar_one()

        if user.hashed_token != hashed_input_token:
            raise HTTPException(status_code=401, detail="Неверный токен")

        logger.info(f"Пользователь с токеном {token} найден")

        salary_data_query = select(SalaryData).where(SalaryData.user_id == user.id)
        salary_data_result = await db.execute(salary_data_query)
        salary_data = salary_data_result.fetchone()

        if datetime.datetime.utcnow() - user.token_live_time >= datetime.timedelta(seconds=40):
            raise HTTPException(status_code=404, detail="Время действия токена истекло, запросите снова")

        if not salary_data:
            raise HTTPException(status_code=404, detail="Данные о зарплате не найдены")

        return {
            "user_id": salary_data[0].user_id,
            "user_name": user.user_name,
            "user_middle_name": user.user_middle_name,
            "user_last_name": user.user_last_name,
            "salary_size": salary_data[0].salary_size,
            "last_update": salary_data[0].time_update,
        }

    except HTTPException:
        raise

    except Exception as err:
        logger.info(f"Ошибка при поиске пользователя по токену: {err}")
        raise HTTPException(status_code=500, detail=f"Внутренняя ошибка сервера {err}")


