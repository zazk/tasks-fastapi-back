import enum
from database import Base
from sqlalchemy import Column, Integer, String, Boolean, Enum

class KindEnum(enum.Enum):
  active = 'Active'
  archived = 'Archived'
  deleted = 'Deleted'

class Tasks(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, primary_key=False, index=True)
    description = Column(String, index=False)
    status = Column(Boolean, default=True)
    typeTask = Column(Enum(KindEnum), default=KindEnum.active)