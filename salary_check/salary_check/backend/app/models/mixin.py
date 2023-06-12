from datetime import datetime
from sqlalchemy import DateTime, Column

from sqlalchemy.orm import declarative_mixin


@declarative_mixin
class Timestamp:
    time_update = Column(DateTime, default=datetime.now())
