from sqlalchemy import insert
from app.core.models.listing import Listing
from sqlalchemy.orm import Session
from pydantic import BaseModel


class ListingUpsert(BaseModel):
    title: str
    description: str
    price_cents: int
    image_urls: list[str]
    market_id: int
    seller_id: int


def _map_listing_to_dict(listing: ListingUpsert) -> dict:
    return {
        "title": listing.title,
        "description": listing.description,
        "price_cents": listing.price_cents,
        "image_urls": listing.image_urls,
        "market_id": listing.market_id,
        "seller_id": listing.seller_id,
    }


class ListingRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, listing: ListingUpsert) -> dict:
        self.session.execute(insert(Listing).values([_map_listing_to_dict(listing)]))
        self.session.commit()
