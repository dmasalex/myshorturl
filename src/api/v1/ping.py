from fastapi import APIRouter, Depends

from di.providers import get_ping_service
from services.ping import PingService

ping_router = APIRouter()


@ping_router.get("/ping", summary="Проверка статуса БД")
async def ping(
    service: PingService = Depends(get_ping_service),
):
    return await service.ping()
