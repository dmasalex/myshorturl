from fastapi import APIRouter

from api.v1.ping import ping_router

own_router = APIRouter()

own_router.include_router(ping_router, tags=["PING"])
