from fastapi import FastAPI
from app.core.config import settings
from app.core.logger import logger

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION
)
logger.info("InsightForge application started")

@app.get("/")
def root():
    return {"message": "Welcome to InsightForge"}


@app.get("/health")
def health():
    return {"status": "healthy"}