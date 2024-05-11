from pydantic import BaseModel


class Config(BaseModel):
    button_id: int
    var_id: int
