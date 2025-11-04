import os
from dotenv import load_dotenv

# Check if we're in production
ENV = os.getenv("ENV", "development")  # Default to "development"
if ENV == "test":
    load_dotenv(".env.test")
elif ENV != "production":
    load_dotenv(".env.dev")  # Load dev variables if not in production
else:
    print("Loading production variables")
    load_dotenv()


class Settings:
    BASE_DATABASE_URL: str = os.getenv("BASE_DATABASE_URL")
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    DATABASE_NAME: str = os.getenv("DATABASE_NAME")
