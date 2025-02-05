from fastapi import FastAPI

from api.handlers import demo

# GET, POST, PUT, PATCH, DELETE


def create_app():
    app = FastAPI(docs_url="/", redoc_url="/docs")
    app.include_router(demo.router)  # attaching router to the main application.
    return app
