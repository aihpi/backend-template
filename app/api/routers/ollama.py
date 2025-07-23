from typing import Annotated

from fastapi import APIRouter
from fastapi.params import Depends

from app.api.views.ollama import OllamaResponseView, OllamaRequestView
from app.core.ollama import ask_ollama_with_prompt
from app.settings import Settings, get_settings

ollama_router = APIRouter()
@ollama_router.post("/ollama", response_model=OllamaResponseView)
async def ask_ollama(
        request: OllamaRequestView,
        settings: Annotated[Settings, Depends(get_settings)]
):
    response = await ask_ollama_with_prompt(settings, request.prompt)
    return {"text": response}