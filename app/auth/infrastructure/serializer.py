from pydantic import BaseModel, EmailStr


class LoginSerializer(BaseModel):
    email: EmailStr
    password: str


class LoginOut(BaseModel):
    token: str
