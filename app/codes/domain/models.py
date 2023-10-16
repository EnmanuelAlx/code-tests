from dataclasses import dataclass


@dataclass
class Code:
    status: int
    name: str

    def __post_init__(self):
        self.validate_status(self.status)
        self.validate_name(self.name)

    def validate_status(self, status):
        if not isinstance(status, int):
            raise ValueError("status must be an integer")
        if len(str(status)) != 2:
            raise ValueError("status must be an integer with length 2")

    def validate_name(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be an string")
        if len(str(name)) != 2:
            raise ValueError("Name must be a string with length 2")

    def to_dict(self):
        return {"status": self.status, "name": self.name}
