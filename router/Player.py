from fastapi import APIRouter,Depends
from typing import List
from db import db_player
from schemas import PlayerBase, PlayerDisplay
from db.database import get_db



router=APIRouter(prefix='/Players' , tags=["Player"])

@router.post("/" , response_model=List[PlayerDisplay])
async def create_palyer(player1:PlayerBase, player2:PlayerBase ,db=Depends(get_db)):
     db_player.create_palyer(db , player1)
     db_player.create_palyer(db, player2)
     items=db_player.read_all_user(db)
     if len(items)<10:
          return items
     else:
          return items[:10]