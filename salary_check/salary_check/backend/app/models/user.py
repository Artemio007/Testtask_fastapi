from app.db.base_class import Base
from fastapi_users import db as usr
from sqlalchemy import Column, String, Boolean, Integer, DateTime
from sqlalchemy.orm import relationship


class User(Base, usr.SQLAlchemyBaseUserTable[int]):
    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String(30))
    user_middle_name = Column(String(30))
    user_last_name = Column(String(30))
    email = Column(String(length=320), unique=True, index=True, nullable=False)
    hashed_password = Column(String(length=1024), nullable=False)
    hashed_token = Column(String(length=1024))
    is_active: bool = Column(Boolean, default=True)
    is_superuser: bool = Column(Boolean, default=False)
    is_verified: bool = Column(Boolean, default=False)
    token_live_time = Column(DateTime, nullable=True)

    salary_data = relationship("SalaryData", backref="user", uselist=False)
