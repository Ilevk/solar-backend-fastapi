from fastapi import APIRouter

from app.routers.chat import router as chat_router

router = APIRouter(prefix="/api/v1")

router.include_router(chat_router, tags=["chat"])
