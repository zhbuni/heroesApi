from typing import Union

from fastapi import FastAPI

from app.api.handlers.hero_info import heroes_router

app = FastAPI(swagger_ui_parameters={"syntaxHighlight": False})
app.include_router(heroes_router)


@app.get("/ping")
def ping():
    return "ping"
