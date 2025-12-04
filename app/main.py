from fastapi import FastAPI
from app.core.config import settings
from app.api.api import api_router

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="API para gestão de portfólio de criptoativos com cotação em tempo real.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

@app.get("/health", tags=["System"])
async def health_check():
    """
    Verifica se a API está online.
    """
    return {"status": "ok", "app_name": settings.PROJECT_NAME}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

app.include_router(api_router, prefix=settings.API_V1_STR)