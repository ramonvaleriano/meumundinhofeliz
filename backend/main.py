from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.config import settings
from app.core.database import ensure_database_exists
from app.core.migrations import run_migrations
from app.routes import router as api_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    ensure_database_exists()
    run_migrations()
    yield


app = FastAPI(title=settings.project_name, lifespan=lifespan)

app.include_router(api_router, prefix="/api")


@app.get("/")
def root():
    return {"status": "ok", "message": "API online"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
