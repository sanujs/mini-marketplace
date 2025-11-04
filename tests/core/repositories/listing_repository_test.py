from app.core.models.listing import Listing
from app.core.repositories.listing_repository import ListingRepository, ListingUpsert
from app.core.repositories.user_repository import UserRepository, UserUpsert
from app.core.repositories.market_repository import MarketRepository, MarketUpsert


def test_create(db_session):
    # First, create a user to be the seller
    ur = UserRepository(db_session)
    user_upsert = UserUpsert(name="Seller User", email="testemail")
    ur.create(user_upsert)
    # Then, create a market to list the item in
    mr = MarketRepository(db_session)
    market_upsert = MarketUpsert(name="Test Market", admin_id=1)
    mr.create(market_upsert)
    # Now, create the listing
    repository = ListingRepository(db_session)
    listing_upsert = ListingUpsert(
        title="Test Listing",
        description="This is a test listing.",
        price_cents=1000,
        image_urls=["http://example.com/image1.jpg", "http://example.com/image2.jpg"],
        market_id=1,
        seller_id=1,
    )
    repository.create(listing_upsert)

    listing = db_session.query(Listing).filter_by(title="Test Listing").first()
    assert listing is not None
    assert listing.title == "Test Listing"
    assert listing.description == "This is a test listing."
    assert listing.price_cents == 1000
    assert listing.image_urls == [
        "http://example.com/image1.jpg",
        "http://example.com/image2.jpg",
    ]
    assert listing.market_id == 1
    assert listing.seller_id == 1
