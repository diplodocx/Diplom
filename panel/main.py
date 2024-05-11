from fastapi import FastAPI
from db import get_configs, create_config
from models import Config

app = FastAPI()


@app.get("/get_configs")
async def root():
    res = get_configs()
    return res


@app.post("/add_config")
async def root(config: Config):
    res = create_config(config)
    return res
