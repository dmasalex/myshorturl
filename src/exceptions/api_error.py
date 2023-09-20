from fastapi import HTTPException


class BadRequestHttpError(HTTPException):
    def __init__(self, detail: str):
        self.detail = detail
