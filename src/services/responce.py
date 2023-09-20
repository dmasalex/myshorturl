from fastapi.responses import JSONResponse

from services.logs import logger


@logger.catch()
def generate_json_response(body: dict | list, status_code: int):
    return JSONResponse(body, status_code=status_code)


@logger.catch()
def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }
