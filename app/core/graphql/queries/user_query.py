import strawberry
from app.db import Database
from app.core.repositories.user_repository import UserRepository
from app.core.graphql.schemas.user_schema import UserSchema


@strawberry.type
class UserQuery:
    @strawberry.field
    def user(self, id: int) -> UserSchema:
        db = Database()
        with db.Session() as session:
            ur = UserRepository(session)
            user = ur.get_by_id(id)
            return UserSchema(id=user.id, name=user.name, email=user.email)
