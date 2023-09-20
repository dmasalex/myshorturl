from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from starlette.status import HTTP_404_NOT_FOUND
from fastapi.responses import RedirectResponse

from dto.urls import URLBaseDTO, URLLongDTO
from services.logs import logger
from services.urls import (
    update_url_service,
    get_short_url_service,
    retrieve_urls_service,
    get_url_from_short_service,
)
from services.utils import generate_short_url
from services.responce import ResponseModel, generate_json_response

urls_router = APIRouter()


@logger.catch()
@urls_router.post(
    "/generate_short_url/{long_url}",
    summary="Получить SHORT-URL",
)
async def get_short_url(
    data: URLLongDTO,
):
    short_hash = generate_short_url(data.long_url)
    url_dto = URLBaseDTO(
        long_url=data.long_url, short_url=short_hash[:5], redirect_count=0
    )
    long_url = jsonable_encoder(url_dto)
    print("lluu--->>>", long_url)
    new_url = await get_short_url_service(long_url)
    print("---->>>", new_url)
    return new_url["short_url"]


@logger.catch()
@urls_router.get("/urls", summary="URLS retrieved")
async def get_urls() -> dict:
    urls = await retrieve_urls_service()
    if urls:
        return ResponseModel(urls, "Students data retrieved successfully")
    return ResponseModel(urls, "Empty list returned")


@logger.catch()
@urls_router.get("/long_url/{short_url}", summary="Get long URL")
async def get_long_url(short_url: str):
    base_url = await get_url_from_short_service(short_url)
    return base_url["long_url"]


@logger.catch()
@urls_router.get(
    "/{short_url}",
    response_class=RedirectResponse,
    status_code=302,
    summary="Redirect for long URL",
)
async def redirect_long_url(short_url: str):
    try:
        base_url = await get_url_from_short_service(short_url)
        redirect_count = base_url["redirect_count"] + 1
        update_data = {"redirect_count": redirect_count}
        await update_url_service(
            id=base_url["id"],
            update_data=update_data,
        )
        return base_url["long_url"]
    except Exception as e:
        return generate_json_response(
            {False: f"{e}"},
            HTTP_404_NOT_FOUND,
        )


@logger.catch()
@urls_router.get(
    "/count/{short_url}",
    summary="Redirect for long URL",
)
async def get_redirect_count(
    short_url: str,
):
    try:
        base_url = await get_url_from_short_service(short_url)
        return base_url["redirect_count"]
    except Exception as e:
        logger.error(e)
        return generate_json_response(
            {False: "URL не найден в БД"},
            HTTP_404_NOT_FOUND,
        )
