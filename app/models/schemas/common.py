from typing import List, Optional
from pydantic import BaseModel


class ErrorResponse(BaseModel):
    message: str
    statusCode: str

class ChatRequest(BaseModel):
    messages: List[str]
    model: str = "solar-1-mini-chat"
    stream: bool = False

class ChatResponse(BaseModel):
    message: str = "OK"
    statusCode: str = "200"
    data: Optional[str]
