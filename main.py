from app.db import Database
from app.core.repositories.user_repository import UserRepository, UserUpsert
from app.core.repositories.market_repository import MarketRepository, MarketUpsert
from app.core.repositories.listing_repository import ListingRepository, ListingUpsert
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from app.core.graphql.schema import schema

graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")


# def main():
#     db = Database()

#     with db.Session() as session:
#         # mr = MarketRepository(session)
#         # mr.create(
#         #     MarketUpsert(name="Electronics", admin_id=1),
#         # )
#         # print("Created market.")
#         # lr  = ListingRepository(session)
#         # lr.create(
#         #     ListingUpsert(
#         #         title="iPhone 13",
#         #         description="A slightly used iPhone 13 in excellent condition.",
#         #         price_cents=69900,
#         #         image_urls=["https://example.com/iphone13-front.jpg", "https://example.com/iphone13-back.jpg"],
#         #         market_id=1,
#         #         owner_id=1,
#         #     ),
#         # )
#         # print("Created listing.")
#         # ur = UserRepository(session)
#         # ur.create(
#         #     UserUpsert(name="Sanuj Syal", email="sanujsyal@gmail.com"),
#         # )
#         # print("Created user.")
#         pass


# if __name__ == "__main__":
#     main()
