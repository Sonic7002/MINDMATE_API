from uuid import UUID
from sqlalchemy.orm import Session
from ..models.msg import Msg
from ..repos.msg_repo import MsgRepo
from ..repos.convo_repo import ConvoRepo
from ..schemas.msg import MsgCreate, MsgRole

class MsgService:
    def __init__(self, msg_repo: MsgRepo, convo_repo: ConvoRepo):
        self.msg_repo = msg_repo
        self.convo_repo = convo_repo

    def create_msg(self, user_id: UUID, convo_id: UUID, data: MsgCreate, db: Session) -> Msg:
        convo = self.convo_repo.get_by_id(db, convo_id)
        if not convo or convo.user_id != user_id:
            raise ValueError("Invalid convo id")
        return self.repo.create(db, user_id, convo_id, data)

    def get_msgs(self, convo_id: UUID, db: Session) -> list[Msg]:
        return self.repo.get_by_convo_id(db, convo_id)

    def get_5_msgs(self, convo_id: UUID, db: Session) -> list[Msg]:
        return self.repo.get_by_convo_id_5(db, convo_id)
