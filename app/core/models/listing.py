from app.db import Base
from sqlalchemy import ForeignKey, Integer, String, DateTime, ARRAY
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func
from datetime import datetime


class Listing(Base):
    __tablename__ = "listings"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255))
    description: Mapped[str] = mapped_column(String(1024))
    price_cents: Mapped[int]
    image_urls: Mapped[list[str]] = mapped_column(ARRAY(String))

    created_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), nullable=False
    )

    # Many to one relationships
    market_id: Mapped[int] = mapped_column(Integer, ForeignKey("markets.id"))
    market: Mapped["Market"] = relationship(back_populates="listings")

    # One to one relationships
    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    owner: Mapped["User"] = relationship(back_populates="listing")
