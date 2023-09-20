import motor.motor_asyncio

URLS_DETAILS = "mongodb://localhost:27037"

url_client = motor.motor_asyncio.AsyncIOMotorClient(URLS_DETAILS)

urls_database = url_client.urls

urls_collection = urls_database.get_collection("urls_collection")
