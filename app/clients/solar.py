from typing import AsyncGenerator

from openai import AsyncOpenAI, APIConnectionError
from retry import retry

from app.core.logger import logger
from app.core.errors.error import OpenAIException
from app.clients import OpenAIClient
from app.core.config import config

class SolarClient(OpenAIClient):
    def __init__(self):
        self.client = AsyncOpenAI(
            api_key=config.OPENAI_API_KEY,
            base_url="https://api.upstage.ai/v1/solar"
        )

    @retry(tries=5, delay=1, backoff=2, exceptions=APIConnectionError)
    async def generate(self, messages: str, model: str = "solar-1-mini-chat", **kwargs) -> str:
        logger.info(f"Generating completion for message: {messages}, model: {model}")
        try:
            response = await self.client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=0,
                **kwargs,
            )

            return response.choices[0].message.content
        except Exception as e:
            logger.error(e)
            raise OpenAIException(f"Completion failed: {e}")

    @retry(tries=5, delay=1, backoff=2, exceptions=APIConnectionError)
    async def stream_generate(self, messages: str, model: str = "solar-1-mini-chat", **kwargs) -> AsyncGenerator[str, None]:
        logger.info(f"Generating stream completion for messages: {messages}, model: {model}")
        try:
            response = await self.client.chat.completions.create(
                model=model,
                messages=messages,
                stream=True,
                **kwargs,
            )

            # return response
            async for chunk in response:
                current_content = chunk.choices[0].delta.content
                if current_content:
                    yield current_content
                else:
                    continue
        except Exception as e:
            logger.error(e)
            raise OpenAIException(f"Completion failed: {e}")
