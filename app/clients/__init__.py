from abc import ABC, abstractmethod

class OpenAIClient(ABC):

    @abstractmethod
    def generate(self, message: str, model: str, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def stream_generate(self, message: str, model: str, **kwargs):
        raise NotImplementedError
