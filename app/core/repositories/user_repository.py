from sqlalchemy import insert
from app.core.models.user import User
from sqlalchemy.orm import Session
from pydantic import BaseModel


class UserUpsert(BaseModel):
    name: str
    email: str


def _map_user_to_dict(user: UserUpsert) -> dict:
    return {
        "name": user.name,
        "email": user.email,
    }


class UserRepository:
    def __init__(self, session: Session):
        self.session = session
    
    def get_by_id(self, user_id: int) -> User | None:
        return self.session.get(User, user_id)

    def create(self, user: UserUpsert) -> dict:
        self.session.execute(insert(User).values([_map_user_to_dict(user)]))
        self.session.commit()
