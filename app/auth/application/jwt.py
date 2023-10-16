from dataclasses import dataclass
from typing import Optional

from app.auth.application.commands import LoginCommand
from app.auth.application.repositories import AbstractAuthRepository
from app.auth.domain.exceptions import UserNotFound
from app.auth.domain.models import User
from app.auth.infrastructure.repositories import AuthRepository
from app.shared.constants import TOKEN


@dataclass
class JWT:
    repository: Optional[AbstractAuthRepository] = None

    def __post_init__(self):
        if not self.repository:
            self.repository = AuthRepository()

    def login(self, cmd: LoginCommand) -> str:
        user = self.repository.get_user_by_email(cmd.email)
        if not user:
            raise UserNotFound(f"User {cmd.email} not found")

        token = self._create_token(user)

        return token

    def _create_token(self, user: User) -> str:
        # TODO: Crear token con JWT
        return TOKEN
