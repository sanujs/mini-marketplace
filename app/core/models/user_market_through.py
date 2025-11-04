from app.db import Base
from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

class UserMarketThrough(Base):
    __tablename__ = "user_market_through"

    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), primary_key=True)
    market_id: Mapped[int] = mapped_column(Integer, ForeignKey("markets.id"), primary_key=True)
