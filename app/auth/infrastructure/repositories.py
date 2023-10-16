from typing import Optional

from app.auth.application.repositories import AbstractAuthRepository
from app.auth.domain import models
from app.auth.infrastructure.models import User
from app.shared.infrastructure.postgres_repository import PostgresRepository


class AuthRepository(AbstractAuthRepository):
    db = PostgresRepository()
    model = User

    @property
    def query(self):
        return self.db.get_session().query(self.model)

    def get_user_by_email(self, email) -> Optional[models.User]:
        user = self.query.filter_by(email=email).first()
        return models.User(email=user.email) if user else None
