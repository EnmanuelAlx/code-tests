from mixer.backend.sqlalchemy import Mixer

from app.codes.infrastructure.models import Code
from app.shared.infrastructure.postgres_repository import PostgresRepository

session = PostgresRepository().get_session()
mixer = Mixer(session)


class TestAuthRoutes:
    ENDPOINT = "codes"

    def setup_method(self):
        self.data = {"status": 12, "name": "AB"}
        self.codes_60 = mixer.cycle(3).blend(Code, status=60, name="AB")
        self.codes_10 = mixer.cycle(3).blend(Code, status=10, name="AB")

    def teardown_method(self):
        session.query(Code).delete()
        session.commit()

    def test_create_code(self, client):
        response = client.post(self.ENDPOINT, json=self.data)
        assert response.status_code == 201

    def test_bad_request_code(self, client):
        self.data["status"] = "123123"
        response = client.post(self.ENDPOINT, json=self.data)
        assert response.status_code == 422

    def test_list_codes_with_status(self, client):
        endpoint = f"{self.ENDPOINT}?code_status=60"
        response = client.get(endpoint)
        assert response.status_code == 200
        assert len(response.json().get("codes")) == 3

    def test_list_codes_without_status(self, client):
        response = client.get(self.ENDPOINT)
        assert response.status_code == 200
        assert len(response.json().get("codes")) == 6
