from uuid import UUID
from sqlalchemy.orm import Session
from ..models.convo import Convo
from ..schemas.convo import ConvoCreate

class ConvoRepo:
    def create(self, db: Session, data: ConvoCreate) -> Convo | None:
        convo = Convo(name = data.name, user_id = data.user_id)
        db.add(convo)
        db.commit()
        db.refresh(convo)
        return convo

    def get_by_id(self, db: Session, convo_id: UUID) ->  Convo | None:
        return db.query(Convo).filter(Convo.id == str(convo_id)).first()

    def get_by_user_id(self, db: Session, user_id: UUID) -> list[Convo]:
        return db.query(Convo).filter(Convo.user_id == str(user_id)).all()

    def save(self, db: Session, convo: Convo) -> Convo:
        db.commit()
        db.refresh(convo)
        return convo
