from bson.objectid import ObjectId
from starlette.status import HTTP_404_NOT_FOUND

from db.base import urls_collection
from dto.urls import URLBaseDTO
from services.logs import logger
from services.responce import generate_json_response


def url_helper(url) -> dict:
    return {
        "id": str(url["_id"]),
        "long_url": url["long_url"],
        "short_url": url.get("short_url", "None"),
        "redirect_count": url.get("redirect_count", 0),
    }


@logger.catch()
async def get_short_url_service(data: URLBaseDTO) -> dict:
    try:
        url = await urls_collection.insert_one(data)
        new_url = await urls_collection.find_one({"_id": url.inserted_id})
        return url_helper(new_url)
    except Exception as e:
        logger.error(e)
        return generate_json_response(
            {"URL уже имеется в БД": f"{e}"},
            HTTP_404_NOT_FOUND,
        )


@logger.catch()
async def get_url_from_short_service(short_url: str):
    try:
        base_url = await urls_collection.find_one({"short_url": short_url})
        url = url_helper(base_url)
        return url
    except Exception as e:
        logger.error(e)
        return generate_json_response(
            {False: "URL не найден в БД"},
            HTTP_404_NOT_FOUND,
        )


@logger.catch()
async def retrieve_urls_service():
    urls = []
    async for url in urls_collection.find():
        urls.append(url_helper(url))
    return urls


@logger.catch()
async def update_url_service(id: str, update_data: dict):
    urls_collection.update_one({"_id": ObjectId(id)}, {"$set": update_data})
