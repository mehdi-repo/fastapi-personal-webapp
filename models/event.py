from sqlalchemy import Time, Column, ForeignKey, Integer, String, Float, Date
from databse.connection import  Base
from sqlalchemy import Boolean, Column, Enum, Integer, String
from typing import Optional, List



class EventModel(Base):
    __tablename__ = "event"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=False, index=True)
    description = Column(String, unique=False, index=True)
