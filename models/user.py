
from sqlalchemy import Column,String,Integer,Boolean,Enum
from schema.user import Roles
from databse.connection import  Base

class UserModel(Base):
    __tablename__ = "users"
    id=Column(Integer,primary_key=True,index=True)
    email=Column(String,unique=True,index=True)
    username=Column(String,unique=True,index=True)
    password=Column(String,unique=False,index=True)
    is_active=Column(Boolean,default=False)
    role=Column(Enum(Roles),default="user")
