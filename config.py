#config.py

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    API_ID = os.getenv("API_ID")
    API_HASH = os.getenv("API_HASH")
    PHONE_NUMBER = os.getenv("PHONE_NUMBER")
    COINGECKO_BASE_URL = os.getenv("COINGECKO_BASE_URL") # Default CoinGecko API URL
    NEWS_FETCHER_TYPE = os.getenv("NEWS_FETCHER_TYPE")
    API_NEWS_URL = os.getenv("API_NEWS_URL")  # Used if NEWS_FETCHER_TYPE is 'api'

    # Add the SCRAPER_URL to the Config object
    SCRAPER_URL = os.getenv("SCRAPER_URL")
    PAGE_LOAD_TIMEOUT = int(os.getenv("PAGE_LOAD_TIMEOUT", "300000"))

    # Playwright configuration
    PLAYWRIGHT_HEADLESS = os.getenv("PLAYWRIGHT_HEADLESS", "false").lower() in ("true", "1", "t")
    PLAYWRIGHT_SLOW_MO = int(os.getenv("PLAYWRIGHT_SLOW_MO", "2000"))

# MongoDB configuration
    MONGO_URI = os.getenv("MONGO_URI")  # No default value
    DB_NAME = os.getenv("DB_NAME")  # No default value
    MONGO_COLLECTION = os.getenv("MONGO_COLLECTION")  # No default value

    print(f"MONGO_URI: {MONGO_URI}")  # Should be a string
    print(f"DB_NAME: {DB_NAME}")      # Should be a string
    print(f"MONGO_COLLECTION: {MONGO_COLLECTION}")  # Should be a string

config = Config()
