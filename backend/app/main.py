from fastapi import FastAPI

app = FastAPI(
    title="InsightForge",
    version="0.1.0"
)


@app.get("/")
def root():
    return {"message": "Welcome to InsightForge"}


@app.get("/health")
def health():
    return {"status": "healthy"}