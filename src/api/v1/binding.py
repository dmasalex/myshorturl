from fastapi import APIRouter

from api.v1.urls import urls_router

own_router = APIRouter()

own_router.include_router(urls_router, tags=["URLS"])
