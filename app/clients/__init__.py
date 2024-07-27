from typing import AsyncGenerator, List

from openai import AsyncOpenAI, APIConnectionError
from retry import retry

from app.core.logger import logger
from app.core.errors.error import OpenAIException
from app.core.config import config

class OpenAIClient:
    def __init__(self, base_url: str):
        self.client = AsyncOpenAI(
            api_key=config.OPENAI_API_KEY,
            base_url=base_url
        )

    @retry(tries=5, delay=1, backoff=2, exceptions=APIConnectionError)
    async def generate(self, messages: List[str], model: str = "solar-1-mini-chat", **kwargs) -> str:
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
    async def stream_generate(self, messages: List[str], model: str = "solar-1-mini-chat", **kwargs) -> AsyncGenerator[str, None]:
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
