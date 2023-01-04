
from pydantic import BaseModel, EmailStr
from typing import Optional, List



class EventSchema(BaseModel):
    title: EmailStr
    description: str

   
    class Config:
        orm_mode = True
    