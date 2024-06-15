from sqlalchemy.orm.session import Session
from schemas import PlayerBase
from db.models import DbPlayer
from sqlalchemy import desc


def create_player(db:Session , request: PlayerBase ):
    item = db.query(DbPlayer).filter(DbPlayer.name == request.name).first()
    if item:
        if request.status=="WIN":
            item.score=item.score+1
        elif request.status=="LOSE":
            if item.score!=0:
                item.score = item.score - 1
            else:
                item.score = 0

        db.commit()
        db.refresh(item)
        return item

    else:
        player = DbPlayer(
            score=0,
            name=request.name
        )
        db.add(player)
        if request.status=="WIN":
            player.score=1
        db.commit()
        db.refresh(player)
        return player


def read_all_user(db:Session):
         return db.query(DbPlayer).order_by(desc(DbPlayer.score)).all()

