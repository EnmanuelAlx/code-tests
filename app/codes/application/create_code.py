from dataclasses import dataclass
from typing import Optional

from app.codes.application import commands
from app.codes.application.repositories import AbstractCodeRepository
from app.codes.domain.models import Code
from app.codes.infrastructure.repository import CodeRepository


@dataclass
class CreateCode:
    repository: Optional[AbstractCodeRepository] = None

    def __post_init__(self):
        if not self.repository:
            self.repository = CodeRepository()

    def execute(self, cmd: commands.CreateCode):
        code = Code(name=cmd.name, status=cmd.status)
        code = self.repository.create(code)
        return code
