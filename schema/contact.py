from pydantic import BaseModel, EmailStr



class ContactSchema(BaseModel):
    email: EmailStr
    title: str
    description: str

    class Config:
        orm_mode = True
    