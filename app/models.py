from .database import Base
from sqlalchemy import Column, String, Integer, TIMESTAMP, ForeignKey
from datetime import datetime
class Users(Base): 
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name= Column(String, nullable=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)

    jioned_date = Column(TIMESTAMP(datetime.utcnow()), server_default=("now()"))

class Events(Base): 
    __tablename__ = 'events'
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    created_date = Column(TIMESTAMP(datetime.utcnow()), server_default=("now()"))

    owner = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'))


