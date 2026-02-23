from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID
from ...db.session import get_db
from ...schemas.msg import MsgCreate, MsgRead, MsgRole
from ...services.msg_service import MsgService
from ..dependencies.deps import get_msg_service
from ...api.dependencies.auth_deps import get_current_user
from ...models.user import User

router = APIRouter(prefix="/msgs", tags=["msgs"])

@router.post("/{convo_id}", response_model=MsgRead)
def create_msg(data: MsgCreate, convo_id: UUID, current_user: User = Depends(get_current_user), service: MsgService = Depends(get_msg_service), db: Session = Depends(get_db)):
    return service.create_msg(current_user.id, convo_id, data, db)

@router.get("/", response_model=list[MsgRead])
def get_all_msgs(convo_id: UUID, current_user: User = Depends(get_current_user), service: MsgService = Depends(get_msg_service), db: Session = Depends(get_db)):
    return service.get_msgs(current_user.id, convo_id, db)
