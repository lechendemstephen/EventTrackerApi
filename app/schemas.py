from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel): 
    name: Optional[str] = None
    email: EmailStr
    password: str

class User(UserBase): 
    pass 


class LoginBase(BaseModel):
    email: EmailStr
    password: str

class Login(LoginBase): 
    pass 


class EventBase(BaseModel): 
    title: str
    description: str 

class Event(BaseModel): 
    title: str
    description: str 

    class Config: 
        orm_mode = True

class CreateEvent(EventBase): 
    id: int

class TokenData(BaseModel):
    id: str 
