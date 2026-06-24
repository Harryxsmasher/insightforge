from fastapi import FastAPI
from app.core.config import settings
from app.core.logger import logger
from app.modules.dataset.routes import router as dataset_router
from app.modules.analysis.routes import (
    router as analysis_router
)
from app.modules.visualization.routes import router as visualization_router
from app.modules.dashboard.routes import (
    router as dashboard_router
)

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION
)

app.include_router(dataset_router)
app.include_router(analysis_router)
app.include_router(visualization_router)
app.include_router(
    dashboard_router
)

@app.get("/")
def root():
    return {"message":"Welcome to InsightForge"}

@app.get("/health")
def health():
    return {"status":"healthy"}