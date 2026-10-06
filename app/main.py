from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.services.epic import get_latest_earth


app = FastAPI(title="Raspberry Space Lab")

app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")


@app.get("/")
def dashboard(request: Request):
    earth = get_latest_earth()

    return templates.TemplateResponse(
        request=request,
        name="dashboard.html",
        context={
            "earth": earth
        }
    )
