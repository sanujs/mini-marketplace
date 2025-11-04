from sqlalchemy import insert
from app.core.models.market import Market
from sqlalchemy.orm import Session
from pydantic import BaseModel


class MarketUpsert(BaseModel):
    name: str
    admin_id: int


def _map_market_to_dict(market: MarketUpsert) -> dict:
    return {
        "name": market.name,
        "admin_id": market.admin_id,
    }


class MarketRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, market: MarketUpsert) -> dict:
        self.session.execute(insert(Market).values([_map_market_to_dict(market)]))
        self.session.commit()
