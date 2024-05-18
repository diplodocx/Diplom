from pydantic import BaseModel, Field


class Config(BaseModel):
    button_id: int
    var_id: int


class Button(BaseModel):
    button_name: str
    scen_id: int


class Scenario(BaseModel):
    scen_name: str
    scen_desc: str


class Var(BaseModel):
    var_name: str = Field(default='0x00')
    var_type: str
