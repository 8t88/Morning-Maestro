from typing import Any

from fastapi import APIRouter, FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from app.api import api_router

PROJECT_NAME: str = "Dawn Chorus API"
api_prefix: str = "/api/v1"

app = FastAPI(
    title=PROJECT_NAME, openapi_url=f"{api_prefix}/openapi.json"
    )

root_router = APIRouter()


@root_router.get("/")
def index(request: Request) -> Any:
    """Basic HTML response."""
    body = (
        "<html>"
        "<body style='padding: 10px;'>"
        "<h1>Welcome to the API</h1>"
        "<div>"
        "Check the docs: <a href='/docs'>here</a>"
        "</div>"
        "</body>"
        "</html>"
    )

    return HTMLResponse(content=body)


app.include_router(api_router, prefix=api_prefix)
app.include_router(root_router)

