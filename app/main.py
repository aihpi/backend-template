import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .settings import backend_settings

app = FastAPI(title="Backend template API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=backend_settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def main():
    uvicorn.run(
        "app.main:app",
        host=backend_settings.HOST,
        port=backend_settings.PORT,
        reload=backend_settings.DEBUG_MODE
    )

if __name__ == "__main__":
    main()