from fastapi import APIRouter

from app.routers.chat import router as chat_router

router = APIRouter()

router.include_router(chat_router, tags=["chat"])
