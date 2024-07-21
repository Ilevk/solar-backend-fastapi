from typing import List, Dict, AsyncGenerator


from app.clients import OpenAIClient


class ChatService:

    def __init__(self, client: OpenAIClient):
        self.client = client

    def get_message(self, messages: str) -> List[Dict[str, str]]:
        message=[
            {
                "role": "system",
                "content": "You are a helpful assistant." # Please Put Default Prompt Here
            },
            {
                "role": "user",
                "content": "\n".join(messages)
            }
        ]

        return message

    async def chat(self, messages: List[str], model: str='solar-1-mini-chat') -> str:

        return await self.client.generate(self.get_message(messages), model)

    async def stream_chat(self, messages: List[str], model: str='solar-1-mini-chat') -> AsyncGenerator:

        return self.client.stream_generate(self.get_message(messages), model)
