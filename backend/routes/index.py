from fastapi import APIRouter

from .health_check import health_check_router
from .query_maker import query_maker_router

api_router = APIRouter()


@api_router.get("/")
async def root():
    return {"message": "Welcome to python boilerplate!"}


api_router.include_router(health_check_router, prefix="", tags=["Check Server Health"])
api_router.include_router(query_maker_router, prefix="", tags=["generate query and run it"])
