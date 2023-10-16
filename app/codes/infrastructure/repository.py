from dataclasses import dataclass

from app.codes.application.repositories import AbstractCodeRepository
from app.codes.domain import models
from app.codes.infrastructure.models import Code
from app.shared.infrastructure.postgres_repository import PostgresRepository


@dataclass
class CodeRepository(AbstractCodeRepository):
    db = PostgresRepository()
    model = Code

    @property
    def query(self):
        return self.db.get_session().query(self.model)

    def create(self, code: Code) -> models.Code:
        new_code = Code(name=code.name, status=code.status)
        self.db.get_session().add(new_code)
        self.db.get_session().commit()
        return code

    def list_by_status(self, status) -> list[models.Code]:
        codes = []
        if not status:
            codes = self.query.all()
        else:
            codes = self.query.filter_by(status=status).all()
        return [models.Code(code.status, code.name) for code in codes]
