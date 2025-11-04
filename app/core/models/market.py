from app.db import Base
from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Market(Base):
    __tablename__ = "markets"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(15))
    admin_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))

    # One to many relationships
    listings: Mapped[list["Listing"]] = relationship(back_populates="market")

    # Many to many relationships
    users: Mapped[list["User"]] = relationship(
        secondary="user_market_through", back_populates="markets"
    )
