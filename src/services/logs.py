from loguru import logger

logger.add(
    "logs.log",
    format="{name}-{function}-{time}-{level}-{message}",
    level="INFO",
    enqueue=True,
)
