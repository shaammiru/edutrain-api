from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.inmemory import InMemoryBackend
from routes import account_route

app = FastAPI()


@asynccontextmanager
async def lifespan_context_manager(_):
    """
    Context manager for the FastAPI app lifespan.

    Initializes  FastAPICache with an InMemoryBackend for the duration of the app's lifespan.
    """
    FastAPICache.init(InMemoryBackend())
    yield


app = FastAPI(
    lifespan=lifespan_context_manager,
    title="edutrain-api",
    description="🧪 Edutrain RESTful API made with Python 3.12 and FastAPI",
    version="1.0.0",
)


app.include_router(account_route.api_router)
