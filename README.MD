# WeDraw

WeDraw Backend project

#### Project for all kind artists where they can share their art-works, have a paid subs and start auctions

![alt text](https://img.shields.io/badge/python-3.11.2-orange)

## Technology stack

1. FastAPI
2. SQLAlchemy + Alembic
3. PostgreSQL + Redis
4. Docker, docker compose
5. S3

## Run

#### Run local environment stack
```shell
docker-compose up -d --build
```

#### Export local envs
```shell
cat .env.example > .env.local

export $(grep -v "^#" .env.local | xargs)
```

#### Install poetry
```shell
pip install poetry
```

#### Install the project dependencies
```shell
cd src && poetry install
```

#### Spawn a shell within the virtual environment
```shell
poetry shell
```

#### Run the server
```shell
uvicorn main:app --reload
```