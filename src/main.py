from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routes import image_content

app = FastAPI(
    title="Online Museum API",
    description="API for managing online museum content",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(image_content.router)

@app.get("/")
def read_root():
    """Root endpoint for health checks"""
    return {"status": "healthy"}
