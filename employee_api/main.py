from fastapi import FastAPI

from .api import employees
from .core.config import settings

app = FastAPI(
    title=settings.app_name,
    docs_url="/docs",
    openapi_url="/openapi.json",
)


@app.get("/health")
def health():
    return {"status": "ok"}


# Routers
app.include_router(employees.router, prefix="/api")
