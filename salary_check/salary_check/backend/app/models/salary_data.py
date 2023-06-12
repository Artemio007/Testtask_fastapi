from app.db.base_class import Base
from app.models.mixin import Timestamp
from sqlalchemy import Column, Float, ForeignKey, Integer


class SalaryData(Base, Timestamp):
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"), unique=True)
    salary_size = Column(Float, default=False)

