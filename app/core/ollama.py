from typing import Annotated

import httpx
import json
from app.settings import Settings


async def ask_ollama_with_prompt(
        settings: Settings,
        prompt: str
) -> str:
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{settings.ollama_url}/api/generate",
            json={"model": settings.ollama_model, "prompt": prompt},
            timeout=30.0
        )
        response.raise_for_status()  # Raises exception if status not 200-299
        return parse_ollama_response(response.text)

def parse_ollama_response(raw_text: str) -> str:
    lines = raw_text.strip().split("\n")
    full_response = []

    for line in lines:
        obj = json.loads(line)
        # Append the "response" chunk
        full_response.append(obj.get("response", ""))
        # If "done" is true, break early
        if obj.get("done", False):
            break

    return "".join(full_response)
