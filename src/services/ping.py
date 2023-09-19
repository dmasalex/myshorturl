from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from services.logs import logger


class PingService:
    def __init__(self, session: AsyncSession):
        self.session = session

    @logger.catch()
    async def ping(self):
        result = await self.session.execute(text("SELECT version();"))
        return result.scalars().all()
