FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10

WORKDIR /backend-developer-test

RUN useradd --home-dir /home/user -g users user && \
    chown user:users .

COPY --chown=user:users ./app ./app
COPY --chown=user:users ./requirements ./requirements
COPY --chown=user:users ./tests ./tests
COPY --chown=user:users ./migrations ./migrations
COPY --chown=user:users ./alembic.ini .

RUN pip install -r ./requirements/common.txt \
    -r ./requirements/development.txt