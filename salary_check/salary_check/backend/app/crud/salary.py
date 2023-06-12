import logging
from sqlalchemy.future import select
from app.db.session import get_async_session
from app.models.salary_data import SalaryData
from app.api.api import fastapi_users

logger = logging.getLogger('salary_check')
current_user = fastapi_users.current_user()


async def create_salary_size_data(db: get_async_session, user_id: int, salary_size: float) -> SalaryData:
    try:
        async with db as session:
            db_salarydata = await session.execute(select(SalaryData).where(SalaryData.user_id == user_id))
            curr = db_salarydata.scalar()

            if curr:
                curr.salary_size = salary_size
            else:
                curr = SalaryData(
                    user_id=user_id,
                    salary_size=salary_size,
                )
                session.add(curr)

            await session.commit()
            await session.refresh(curr)
            return curr

    except Exception as err:
        print(err)
        logger.info(f"Have an error in crud/create create_salary_size_data {err}")

