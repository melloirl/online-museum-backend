from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .env import get_settings
from .routes import image_content

settings = get_settings()

app = FastAPI(
    title="Museu Online",
    description="API para gerenciamento de experiências digitais",
    version="0.0.1",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(image_content.router)


@app.get("/")
def read_root():
    return {"status": "healthy", "env": settings.env}
