from pydantic import BaseModel, validator


class CreateCodeSerializer(BaseModel):
    status: int
    name: str

    @validator("status")
    def validate_status(cls, v):
        if not isinstance(v, int):
            raise ValueError("status must be an integer")
        if len(str(v)) != 2:
            raise ValueError("status must be a two-digit number")
        return v

    @validator("name")
    def validate_name(cls, v):
        if not isinstance(v, str):
            raise ValueError("name must be a string")
        if len(v) != 2:
            raise ValueError("name must be a two-character string")
        return v


class CreateCodeOut(BaseModel):
    status: int
    name: str


class ListCodesOut(BaseModel):
    codes: list[CreateCodeOut]
