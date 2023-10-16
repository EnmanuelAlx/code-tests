from abc import ABC
from dataclasses import dataclass
from typing import Optional

from app.auth.domain.models import User


@dataclass
class AbstractAuthRepository(ABC):
    def get_user_by_email(self, email) -> Optional[User]:
        raise NotImplementedError
