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

class Event(EventBase): 
    pass 

class TokenData(BaseModel):
    id: str 
