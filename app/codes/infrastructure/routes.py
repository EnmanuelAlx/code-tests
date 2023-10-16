from fastapi import APIRouter, Query, status
from fastapi.responses import JSONResponse

from app.codes.application import commands
from app.codes.application.create_code import CreateCode
from app.codes.application.list_codes import ListCodes
from app.codes.infrastructure.serializers import (
    CreateCodeOut,
    CreateCodeSerializer,
    ListCodesOut,
)


class CodeRouter(APIRouter):
    def __init__(self, *args, **kwargs):
        super().__init__()
        # TODO Colocar middleware para verificar se o usuário está logado
        self.add_api_route(
            "/",
            self.create,
            methods=["POST"],
            response_model=CreateCodeOut,
        )
        self.add_api_route(
            "/",
            self.list,
            methods=["GET"],
            response_model=ListCodesOut,
        )

    async def create(self, data: CreateCodeSerializer) -> CreateCodeSerializer:
        cmd = commands.CreateCode(status=data.status, name=data.name)
        code = CreateCode().execute(cmd)
        code_dict = code.to_dict()
        return JSONResponse(
            content={"code": code_dict}, status_code=status.HTTP_201_CREATED
        )

    async def list(self, code_status: int = Query(None)):
        cmd = commands.ListCodes(status=code_status)
        codes = ListCodes().execute(cmd)
        codes = [code.to_dict() for code in codes]
        return JSONResponse(
            content={"codes": codes}, status_code=status.HTTP_200_OK
        )
