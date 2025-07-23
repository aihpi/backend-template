from pydantic import BaseModel


class OllamaRequestView(BaseModel):
    prompt: str


class OllamaResponseView(BaseModel):
    text: str
