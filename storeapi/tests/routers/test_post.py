import pytest
import pytest_asyncio
from httpx import AsyncClient


async def create_post(body: str, client: AsyncClient) -> dict:
    response = await client.post("/post", json={"body": body})
    return response.json()


@pytest_asyncio.fixture()
async def created_post(async_client: AsyncClient) -> dict:
    return await create_post("Test post body", async_client)


@pytest.mark.anyio
async def test_create_post(async_client: AsyncClient):
    body = "Test Post"
    response = await async_client.post("/post", json={"body": body})

    assert response.status_code == 201
    assert {"id": 0, "body": body}.items() <= response.json().items()


@pytest.mark.anyio
async def test_create_post_with_missing_data(async_client: AsyncClient):
    response = await async_client.post("/post", json={})

    assert response.status_code == 422


@pytest.mark.anyio
async def test_get_all_posts(async_client: AsyncClient, created_post: dict):
    response = await async_client.get("/post")

    assert response.status_code == 200
    assert response.json() == [created_post]