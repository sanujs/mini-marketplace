import strawberry
from app.core.graphql.queries.user_query import UserQuery

@strawberry.type
class Query(UserQuery):
    pass

schema = strawberry.Schema(Query)