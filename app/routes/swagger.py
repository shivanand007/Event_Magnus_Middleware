# Swagger Imports
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from fastapi.responses import HTMLResponse

# Router Import
from fastapi import FastAPI
from fastapi import APIRouter

#swagger_app = FastAPI()

swagger_router = APIRouter()

def custom_swagger_ui_html():
    openapi_url = swagger_router.openapi_url
    swagger_ui = get_swagger_ui_html(openapi_url, title="Webhook Documentation")
    return HTMLResponse(content=swagger_ui)

@swagger_router.get("/docs", tags=["Home"])
async def get_documentation():
    return custom_swagger_ui_html()

@swagger_router.get("/openapi.json", tags=["Home"])
async def get_openapi_json():
    return get_openapi(
        title="Task API",
        version="1.0.0",
        description="This is a simple API to manage tasks",
        routes=[router.routes],
    )

#swagger_app.include_router(swagger_router)