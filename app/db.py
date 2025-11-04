from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from app.config import Settings


class Base(DeclarativeBase):
    pass


class Database:
    def __init__(self):
        self.engine = create_engine(
            Settings.DATABASE_URL, echo=False
        )
        self.Session = sessionmaker(self.engine)
