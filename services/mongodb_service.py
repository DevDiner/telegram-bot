# services/mongodb_service.py
import logging
from motor.motor_asyncio import AsyncIOMotorClient
from config import config

logger = logging.getLogger(__name__)

class MongoDBService:
    def __init__(self, uri: str, db_name: str, collection_name: str):
        # Log values to ensure they are strings
        logger.info(f"Connecting to MongoDB with URI: {uri}")
        logger.info(f"Database name: {db_name}")
        logger.info(f"Collection name: {collection_name}")
        
        # Check if the db_name and collection_name are strings
        if not isinstance(db_name, str) or not isinstance(collection_name, str):
            raise TypeError("Database and Collection names must be strings")

        self.client = AsyncIOMotorClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def get_collection(self):
        return self.collection

    async def close(self):
        await self.client.close()

# Instantiate the MongoDB service using configuration values
db_service = MongoDBService(config.MONGO_URI, config.DB_NAME, config.MONGO_COLLECTION)
db = db_service.get_collection()
