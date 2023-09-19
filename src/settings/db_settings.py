from pydantic import BaseSettings, Field


class DBSettings(BaseSettings):
    DB_USER: str = Field(env="DB_USER", default="urluser")
    DB_PASS: str = Field(env="DB_PASS", default="qwe123")
    DB_PORT: str = Field(env="DB_PORT", default="5435")
    DB_HOST: str = Field(env="DB_HOST", default="localhost")
    DB_NAME: str = Field(env="DB_NAME", default="url_bd")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = DBSettings()
