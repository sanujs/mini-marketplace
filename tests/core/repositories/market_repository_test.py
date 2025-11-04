from app.core.models.market import Market
from app.core.repositories.market_repository import MarketRepository, MarketUpsert
from app.core.repositories.user_repository import UserRepository, UserUpsert

def test_create(db_session):
    ur = UserRepository(db_session)
    user_upsert = UserUpsert(name="Test User", email="testemail")
    ur.create(user_upsert)

    repository = MarketRepository(db_session)
    market_upsert = MarketUpsert(name="Test Market", admin_id=1)
    repository.create(market_upsert)

    market = db_session.query(Market).filter_by(name="Test Market").first()
    assert market is not None
    assert market.name == "Test Market"
    assert market.admin_id == 1