from pydantic import Field, BaseModel


class URLOutputDTO(BaseModel):
    id: str = Field(...)
    long_url: str = Field(...)
    short_url: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "id": "650aa43dde2e26db314f2c63",
                "long_url": "https://mail.rambler.ru/",
            }
        }


class URLShortDTO(BaseModel):
    short_url: str = Field(...)


class URLLongDTO(BaseModel):
    long_url: str = Field(...)

    class Config:
        schema_extra = {"example": {"long_url": "https://mail.rambler.ru/"}}


class URLBaseDTO(BaseModel):
    long_url: str = Field(...)
    short_url: str = Field(...)
    redirect_count: int = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "long_url": "https://mail.rambler.ru/",
                "short_url": "short_url",
            }
        }
