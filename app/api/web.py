from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from app.api.routes.health import router as health_router
from app.api.routes.chat import router as chat_router

app = FastAPI(
    title="Versa IA",
    version="1.0.0"
)

app.include_router(health_router)
app.include_router(chat_router)

BASE_DIR = Path(__file__).resolve().parents[2]

WEB_DIR = BASE_DIR / "web"

app.mount(
    "/static",
    StaticFiles(directory=WEB_DIR / "static"),
    name="static"
)


@app.get("/", response_class=HTMLResponse)
async def home():

    with open(
        WEB_DIR / "templates" / "index.html",
        encoding="utf-8"
    ) as html:

        return HTMLResponse(html.read())