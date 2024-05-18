from fastapi import FastAPI
import db
from models import Config, Button, Scenario, Var

app = FastAPI()


@app.get("/get_scens")
async def root():
    res = db.get_scens()
    return res


@app.post("/add_scen")
async def root(scen: Scenario):
    res = db.create_scen(scen)
    return res


@app.get("/get_buttons")
async def root():
    res = db.get_buttons()
    return res


@app.post("/add_button")
async def root(button: Button):
    res = db.create_button(button)
    return res

@app.get("/get_vars")
async def root():
    res = db.get_vars()
    return res


@app.post("/add_var")
async def root(var: Var):
    res = db.create_var(var)
    return res

@app.get("/get_configs")
async def root():
    res = db.get_configs()
    return res


@app.post("/add_config")
async def root(config: Config):
    res = db.create_config(config)
    return res
