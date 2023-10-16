import pytest

from app.codes.domain.models import Code


class TestValidators:
    def setup_method(self):
        self.data = {"status": 10, "name": "AB"}

    def test_valid_code(self):
        assert Code(**self.data)

    def test_invalid_code_status(self):
        self.data["status"] = 1
        with pytest.raises(ValueError):
            Code(**self.data)

    def test_invalid_code_name(self):
        self.data["name"] = "123"
        with pytest.raises(ValueError):
            Code(**self.data)
