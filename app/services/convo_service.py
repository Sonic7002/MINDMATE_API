from uuid import UUID
from sqlalchemy.orm import Session
from ..models.convo import Convo
from ..repos.convo_repo import ConvoRepo
from ..schemas.convo import ConvoCreate, ConvoPatch

class ConvoService:
    def __init__(self, repo: ConvoRepo):
        self.repo = repo

    def create_convo(self, data: ConvoCreate, db: Session) -> Convo:
        return self.repo.create(db, data)

    def get_convo(self, convo_id: UUID, db: Session) -> Convo | None:
        return self.repo.get_by_id(db, convo_id)
    
    def get_convos(self, user_id: UUID, db: Session) -> list[Convo]:
        return self.repo.get_by_user_id(db, user_id)

    def edit_convo(self, convo_id: UUID, data: ConvoPatch, db: Session) -> Convo:
        convo = self.get_convo(convo_id, db)
        if not convo:
            return None
        updates = data.model_dump(exclude_unset=True)

        for field, value in updates.items():
            setattr(convo, field, value)

        return self.repo.save(db, convo)
