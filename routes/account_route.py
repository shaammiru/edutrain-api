from fastapi import APIRouter
from fastapi_cache.decorator import cache

api_router = APIRouter()

CACHING_TIME_IN_SECONDS = 600


@api_router.get("/users", tags=["Users"])
@cache(expire=CACHING_TIME_IN_SECONDS)
async def get_all_async():
    return "This is the list of all users"
