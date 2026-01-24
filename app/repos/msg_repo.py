from uuid import UUID
from sqlalchemy.orm import Session
from ..models.msg import Msg
from ..schemas.msg import MsgCreate

class UserRepo:
    def create(self, db: Session, data: MsgCreate) -> Msg | None:
        msg = Msg(user_id = data.user_id, convo_id = data.convo_id)
        db.add(msg)
        db.commit()
        db.refresh(msg)
        return msg

    def get_by_convo_id(self, db: Session, convo_id: UUID) ->  list[Msg]:
        return db.query(Msg).filter(Msg.convo_id == str(convo_id)).all()

    def get_by_convo_id_5(self, db: Session, convo_id: UUID) -> list[Msg]:
        msgs = db.query(Msg).filter(Msg.convo_id == str(convo_id)).order_by(Msg.created_at.desc()).limit(5).all()
        return msgs.reverse()
