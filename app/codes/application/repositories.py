from abc import ABC

from app.codes.domain.models import Code


class AbstractCodeRepository(ABC):
    def create(self, code: Code) -> Code:
        raise NotImplementedError

    def list_by_status(self, status) -> list[Code]:
        raise NotImplementedError
