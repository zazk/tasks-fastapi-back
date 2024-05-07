import enum
from database import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Enum
from sqlalchemy.orm import relationship

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
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("Users", back_populates="tasks")


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, primary_key=False, index=True)
    email = Column(String, index=False)
    fullname = Column(String, index=False)
    password = Column(String, index=False)
    token = Column(String, index=False)
    status = Column(Boolean, default=True)
    tasks = relationship("Tasks", back_populates="user")
