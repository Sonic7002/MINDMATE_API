from uuid import UUID
from sqlalchemy.orm import Session
from ..models.msg import Msg
from ..repos.msg_repo import MsgRepo
from ..schemas.msg import MsgCreate, MsgRole

class MsgService:
    def __init__(self, repo: MsgRepo):
        self.repo = repo

    def create_msg(self, data: MsgCreate, db: Session) -> Msg:
        return self.repo.create(db, data)

    def get_msgs(self, convo_id: UUID, db: Session) -> list[Msg]:
        return self.repo.get_by_convo_id(db, convo_id)

    def get_5_msgs(self, convo_id: UUID, db: Session) -> list[Msg]:
        return self.repo.get_by_convo_id_5(db, convo_id)
