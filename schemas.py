from pydantic import BaseModel
from enum import Enum

class statusEnum(str , Enum):
    WIN = "WIN"
    LOSE = "LOSE"

class PlayerBase(BaseModel):
    name:str
    status: statusEnum


class PlayerDisplay(BaseModel):
    name:str
    score:int
    class Config:
        from_attributes = True




