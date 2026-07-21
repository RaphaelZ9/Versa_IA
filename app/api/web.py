from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

app = FastAPI(
    title="Versa IA",
    version="1.0.0"
)

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