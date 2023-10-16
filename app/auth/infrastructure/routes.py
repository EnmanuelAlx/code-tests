from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from app.auth.application.jwt import JWT
from app.auth.infrastructure.serializer import LoginOut, LoginSerializer


class AuthRouter(APIRouter):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.add_api_route(
            "/login", self.login, methods=["POST"], response_model=LoginOut
        )
        self.login_method = JWT()

    async def login(self, data: LoginSerializer) -> JSONResponse:
        token = self.login_method.login(data)
        return JSONResponse(
            content={"token": token}, status_code=status.HTTP_200_OK
        )
