from fastapi import APIRouter, FastAPI, Request

from controllers.health_check.index import health_check

app = FastAPI()
health_check_router = APIRouter()


@health_check_router.get("/health-check")
async def check_health(request: Request):
    return await health_check(request)
