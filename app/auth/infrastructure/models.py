from sqlalchemy import Column, String

from app.shared.infrastructure.models import BaseModel


class User(BaseModel):
    __tablename__ = "users"
    email = Column(String, unique=True, nullable=False)
