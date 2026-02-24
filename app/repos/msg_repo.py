from uuid import UUID
from sqlalchemy.orm import Session
from ..models.msg import Msg
from ..schemas.msg import MsgCreate, MsgRole

class MsgRepo:
    def create(self, db: Session, user_id:UUID, convo_id: UUID, data: MsgCreate) -> Msg | None:
        msg = Msg(user_id = str(user_id), convo_id = str(convo_id), role = data.role, content= data.content)
        db.add(msg)
        db.commit()
        db.refresh(msg)
        return msg

    def get_by_convo_id(self, db: Session, convo_id: UUID) ->  list[Msg]:
        return db.query(Msg).filter(Msg.convo_id == str(convo_id)).all()

    def get_by_convo_id_5(self, db: Session, convo_id: UUID) -> list[Msg]:
        msgs = db.query(Msg).filter(Msg.convo_id == str(convo_id)).order_by(Msg.created_at.desc()).limit(5).all()
        return msgs.reverse()
