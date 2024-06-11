from db.database import Base
from sqlalchemy import Column, Integer, String


class DbPlayer(Base):
    __tablename__='player'
    name=Column(String, primary_key=True , unique=True)
    score=Column(Integer)


    