from typing import List, Dict, AsyncGenerator
from abc import ABC, abstractmethod

class OpenAIClient(ABC):

    @abstractmethod
    def generate(self, messages: List[Dict[str, str]], model: str, **kwargs) -> str:
        """
        Generate completion from OpenAI API

        Args:
            messages (List[Dict[str, str]]): List of messages
            model (str): Model name

        Raises:
            NotImplementedError
        """
        raise NotImplementedError

    @abstractmethod
    def stream_generate(self, messages: List[Dict[str, str]], model: str, **kwargs) -> AsyncGenerator:
        """
        Generate stream completion from OpenAI API

        Args:
            messages (List[Dict[str, str]]): List of messages
            model (str): Model name

        Raises:
            NotImplementedError

        Returns:
            AsyncGenerator
        """
        raise NotImplementedError
