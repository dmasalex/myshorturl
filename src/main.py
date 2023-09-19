from fastapi import FastAPI

from api.v1.binding import own_router

app = FastAPI()

app.include_router(own_router)
