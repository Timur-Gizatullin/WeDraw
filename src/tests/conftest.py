import asyncio
import os
import typing

import alembic.command
import pytest
import pytest_asyncio
from aioboto3.session import Session
from alembic.config import Config
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession

from core.config import settings
from db import session
from db.redis import AsyncRedis, get_redis, get_redis_connection
from db.session import get_engine
from main import app
from tests.utils import create_database, database_exists, drop_database, get_random_str

pytestmark = pytest.mark.asyncio


@pytest.fixture(scope="session")
def mock_settings() -> None:
    settings.cache_clear()
    os.environ["ENVIRONMENT"] = "test"


def get_failed_boto3_session() -> Session:
    return Session(
        aws_access_key_id=settings().S3_ACCESS_KEY_ID,
        aws_secret_access_key=get_random_str(),
        region_name=settings().S3_ACCESS_KEY_ID,
    )


@pytest.fixture(scope="session")
def event_loop() -> typing.Generator[asyncio.AbstractEventLoop, None, None]:
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture(scope="session")
async def async_db_engine(mock_settings) -> typing.AsyncGenerator[AsyncEngine, None]:
    if await database_exists(settings().postgres_dsn):
        await drop_database(settings().postgres_dsn)

    await create_database(settings().postgres_dsn)

    engine = get_engine()
    await engine.dispose()

    yield engine

    await engine.dispose()
    await drop_database(settings().postgres_dsn)


@pytest.fixture(scope="session")
def apply_migrations() -> typing.Generator[None, None, None]:
    config = Config(os.path.join(settings().BASE_DIR, "alembic.ini"))
    config.set_main_option("script_location", os.path.join(settings().BASE_DIR, "migrations"))
    alembic.command.upgrade(config, "head")
    yield
    alembic.command.downgrade(config, "base")


@pytest_asyncio.fixture(scope="function")
async def async_db_session(async_db_engine: AsyncEngine, apply_migrations) -> typing.AsyncGenerator[AsyncSession, None]:
    async with async_db_engine.connect() as conn:
        async with conn.begin() as transaction:
            session = AsyncSession(bind=conn, expire_on_commit=False)

            yield session

            await transaction.rollback()


@pytest_asyncio.fixture(scope="function")
async def async_redis_client() -> typing.AsyncGenerator[AsyncRedis, None]:
    async with get_redis_connection() as redis:
        yield redis
        await redis.flushdb()


@pytest.fixture(scope="function")
def s3_session() -> Session:
    return Session(
        aws_access_key_id=settings().S3_ACCESS_KEY_ID,
        aws_secret_access_key=settings().S3_ACCESS_KEY_ID,
        region_name=settings().S3_ACCESS_KEY_ID,
    )


@pytest_asyncio.fixture(scope="function")
async def api_client(
    async_db_session: AsyncSession, async_redis_client: AsyncRedis
) -> typing.AsyncGenerator[AsyncClient, None]:
    app.dependency_overrides[session.get_session] = lambda: async_db_session
    app.dependency_overrides[get_redis] = lambda: async_redis_client

    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client
