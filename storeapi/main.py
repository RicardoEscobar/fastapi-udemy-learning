from contextlib import asynccontextmanager
from fastapi import FastAPI
from storeapi.routers.post import router as post_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await post_router.startup()
    yield
    await post_router.shutdown()


app = FastAPI(lifespan=lifespan)
app.include_router(post_router)
