from dataclasses import dataclass


@dataclass
class CreateCode:
    status: int
    name: str


@dataclass
class ListCodes:
    status: int
