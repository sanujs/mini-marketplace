from app.db import Base
from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from sqlalchemy.sql import func


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(100), unique=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), nullable=False
    )

    # Many to many relationships
    markets: Mapped[list["Market"]] = relationship(
        secondary="user_market_through", back_populates="users"
    )

    # One to many relationships
    listings: Mapped[list["Listing"]] = relationship(back_populates="seller")