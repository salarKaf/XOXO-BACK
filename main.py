from fastapi import FastAPI
from db import models 
from db.database import engine
from router import Player



app = FastAPI()
app.include_router(Player.router)
models.Base.metadata.create_all(engine)


@app.get('/')
def hello():
    return {"message":'hello world!'}