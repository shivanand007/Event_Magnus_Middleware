from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.utils import logger


app = FastAPI(title="Event Magnus",
            description="Standard Webhook Middleware Designed to transfer Digital Events in Realtime",
            version="1.1.0",
            #openapi_url="/openapi.json",
            docs_url="/docs",
            redoc_url="/redoc")


from app.routes import event_router,swagger_router,register_router,server_router #event_app,swagger_app
# Include the routes in the app
#app.mount("/event", event_app)
#app.mount("/swagger", swagger_app)

app.include_router(swagger_router)
app.include_router(event_router)
app.include_router(register_router)
app.include_router(server_router)


if __name__ == "__main__":
    import uvicorn
    logger.info("---------------New Request Trigger-------------")
    uvicorn.run(app, host="127.0.0.1", port=8000)




