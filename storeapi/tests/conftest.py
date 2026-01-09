import os
from typing import AsyncGenerator, Generator

import pytest
import pytest_asyncio
from fastapi.testclient import TestClient
from httpx import ASGITransport, AsyncClient

from storeapi.routers.post import comment_table, post_table

os.environ["ENV_STATE"] = "test"

from storeapi.main import app # noqa: E402


@pytest.fixture()
def anyio_backend() -> str:
    return "asyncio"


@pytest.fixture()
def client() -> Generator:
    yield TestClient(app)


@pytest_asyncio.fixture(autouse=True)
async def db() -> AsyncGenerator:
    post_table.clear()
    comment_table.clear()
    yield


@pytest_asyncio.fixture()
async def async_client(client: TestClient) -> AsyncGenerator:
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
        yield ac