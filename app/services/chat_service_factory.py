from typing import Dict

from app.clients import OpenAIClient
from app.services.chat import ChatService

class ChatServiceFactory:
    base_urls: Dict[str, OpenAIClient] = {
        'solar': "https://api.upstage.ai/v1/solar"
    }

    @classmethod
    def get_chat_service(cls, client_name: str = 'solar') -> ChatService:
        return ChatService(OpenAIClient(base_url=cls.base_urls[client_name]))
