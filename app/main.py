from os import getenv

from fastapi import FastAPI

from app.auth.infrastructure.routes import AuthRouter
from app.codes.infrastructure.routes import CodeRouter
from app.shared.infrastructure.postgres_repository import PostgresRepository

DEBUG = getenv("FASTAPI_DEBUG", True)

PostgresRepository.init_db()
app = FastAPI(debug=DEBUG)
app.include_router(AuthRouter(), prefix="/auth")
app.include_router(CodeRouter(), prefix="/codes")
