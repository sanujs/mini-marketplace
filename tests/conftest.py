import pytest
from sqlalchemy import create_engine, text
from app.db import Database, Base
from app.config import Settings
from app.core.models import *


# Postgres DB
@pytest.fixture(scope="session")
def root_engine():
    root_engine = create_engine(
        Settings.BASE_DATABASE_URL,
        isolation_level="AUTOCOMMIT",
        pool_pre_ping=True,  # Add this for better connection handling
    )
    yield root_engine
    root_engine.dispose()


# recreate bitcoin_tracker database for testing
@pytest.fixture(scope="session", autouse=True)
def init_db(root_engine):
    with root_engine.begin() as conn:
        conn.execute(text(f"DROP DATABASE IF EXISTS {Settings.DATABASE_NAME}"))
        conn.execute(text(f"CREATE DATABASE {Settings.DATABASE_NAME}"))

    yield

    with root_engine.begin() as conn:
        conn.execute(
            text(f"""
            SELECT pg_terminate_backend(pg_stat_activity.pid)
            FROM pg_stat_activity
            WHERE pg_stat_activity.datname = '{Settings.DATABASE_NAME}'
        """)
        )
        conn.execute(text(f"DROP DATABASE {Settings.DATABASE_NAME}"))


@pytest.fixture()
def test_engine():
    engine = create_engine(Settings.DATABASE_URL)
    yield engine
    engine.dispose()


@pytest.fixture(autouse=True)
def setup_test_database(test_engine):
    with test_engine.begin() as conn:
        Base.metadata.create_all(conn)

    yield

    with test_engine.begin() as conn:
        Base.metadata.drop_all(conn)


@pytest.fixture()
def db_session():
  database = Database()
  with database.Session() as session:
      yield session
