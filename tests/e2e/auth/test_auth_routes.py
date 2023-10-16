from mixer.backend.sqlalchemy import Mixer

from app.auth.infrastructure.models import User
from app.shared.infrastructure.postgres_repository import PostgresRepository

session = PostgresRepository().get_session()
mixer = Mixer(session)


class TestAuthRoutes:
    ENDPOINT = "auth/login"

    def setup_method(self):
        mixer.blend(User, email="enmanuel@gmail.com")
        self.data = {"email": "enmanuel@gmail.com", "password": "123123"}

    def teardown_method(self):
        session.query(User).delete()
        session.commit()

    def test_api_login(self, client):
        response = client.post(self.ENDPOINT, json=self.data)
        assert response.status_code == 200

    def test_api_login_bad_email(self, client):
        self.data["email"] = "123123"
        response = client.post(self.ENDPOINT, json=self.data)
        assert response.status_code == 422
