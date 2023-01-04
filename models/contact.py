from sqlalchemy import  Column, Integer, String
from databse.connection import  Base
from sqlalchemy import  Column, Integer, String



class ContactModel(Base):
    __tablename__ = "contact"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=False, index=True)
    title = Column(String, unique=False, index=True)
    description = Column(String, unique=False, index=True)


