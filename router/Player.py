from fastapi import APIRouter,Depends
from fastapi import FastAPI
from typing import List
from db import db_player
from schemas import PlayerBase, PlayerDisplay
from db.database import get_db




router=APIRouter(prefix='/Players' , tags=["Player"])


# router.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:5173","http://127.0.0.1:8000"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# // player2:PlayerBase , response_model=List[PlayerDisplay],

@router.post("/AddScores")
async def create_player(player1: PlayerBase, db=Depends(get_db)):
    return db_player.create_player(db, player1)



@router.get("/ReadScores" , response_model=List[PlayerDisplay])
async def Read_Players(db=Depends(get_db)):
     items= db_player.read_all_user(db)
     if len(items)<10:
          return items
     else:
          return items[:10]



# @router.middleware("http")
# async def add_middle_ware(request:Request , create_player,):
#      start_time=time.time()
#      response=await create_player(request , db=Depends(get_db))
#      duration=time.time()-start_time
#      response.headers['duration']=str(duration)
#      return response

