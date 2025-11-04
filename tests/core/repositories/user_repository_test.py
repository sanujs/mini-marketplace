from app.core.models.user import User
from app.core.repositories.user_repository import UserRepository, UserUpsert

def test_create(db_session):
    repository = UserRepository(db_session)
    user_upsert = UserUpsert(name="Test User", email="test@example.com")
    repository.create(user_upsert)

    user = db_session.query(User).filter_by(email="test@example.com").first()
    assert user is not None
    assert user.name == "Test User"
    assert user.email == "test@example.com"