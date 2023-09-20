from services.logs import logger


@logger.catch()
def generate_short_url(long_url: str) -> str:
    hash_long_url = hash(long_url)
    logger.info(f"Create short-url {hash_long_url}")
    return hex(hash_long_url)
