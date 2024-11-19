from pydantic import BaseModel, EmailStr, model_validator
from typing import Optional

class EmployeeCreate(BaseModel):
    name: str
    position: str
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    name: str
    position: str
    email: EmailStr
    