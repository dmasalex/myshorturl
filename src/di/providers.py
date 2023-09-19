from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db.base import get_session
from services.logs import logger
from services.ping import PingService


@logger.catch()
async def get_ping_service(session: AsyncSession = Depends(get_session)) -> PingService:
    return PingService(session=session)
