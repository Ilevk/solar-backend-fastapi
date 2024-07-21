class BaseAPIException(Exception):
    def __init__(self, code: str, message: str):
        self.code = code
        self.message = message


class BaseAuthException(Exception):
    def __init__(self, code: str, message: str):
        self.code = code
        self.message = message

class OpenAIException(BaseAPIException):
    def __init__(self, message: str):
        super().__init__("OPENAI_ERROR", message)
