from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import validates

from app.shared.infrastructure.models import BaseModel


class Code(BaseModel):
    __tablename__ = "codes"
    status = Column(Integer, nullable=False)
    name = Column(String, nullable=False)

    @validates("status")
    def validate_status(self, key, value):
        if len(str(value)) != 2:
            raise ValueError(
                "The 'status' field must be a integer of length 2"
            )
        return value

    @validates("name")
    def validate_name(self, key, value):
        if len(value) != 2:
            raise ValueError(
                "The value of 'name' field must be a string of length 2"
            )
        return value
