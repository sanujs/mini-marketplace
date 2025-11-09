import strawberry

@strawberry.type
class UserSchema:
    id: int
    name: str
    email: str