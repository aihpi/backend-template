import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routers.ollama import ollama_router
from .settings import get_settings

backend_settings = get_settings()

app = FastAPI(title="Backend template API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=backend_settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(ollama_router)

def main():
    uvicorn.run(
        "app.main:app",
        host=backend_settings.host,
        port=backend_settings.port,
        reload=backend_settings.debug_mode
    )

if __name__ == "__main__":
    main()