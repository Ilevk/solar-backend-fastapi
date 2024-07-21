from typing import Dict

from app.clients import OpenAIClient
from app.clients.solar import SolarClient
from app.services.chat import ChatService

class ChatServiceFactory:
    clients: Dict[str, OpenAIClient] = {
        'solar': SolarClient
    }

    @classmethod
    def get_chat_service(cls, client_name: str = 'solar') -> ChatService:
        return ChatService(cls.clients[client_name]())
