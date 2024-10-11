# --------------------------------------------------
# Account Route
# --------------------------------------------------

from fastapi import APIRouter
from fastapi_cache.decorator import cache

api_router = APIRouter()

CACHING_TIME_IN_SECONDS = 600


# --------------------------------------------------
# GET Method
# --------------------------------------------------
@api_router.get("/users", tags=["Users"])
@cache(expire=CACHING_TIME_IN_SECONDS)
async def get_all_async():
    return "This is the list of all users"


# --------------------------------------------------
# POST Method
# --------------------------------------------------
@api_router.post("/users", tags=["Users"])
async def create_async():
    return "User created successfully"


# --------------------------------------------------
# PUT Method
# --------------------------------------------------

# --------------------------------------------------
# DELETE Method
# --------------------------------------------------
