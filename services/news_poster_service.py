# services/news_poster_service.py


import sys
import os

sys.path.insert(0, '/root/folder/cointelegraph_news_scraper')
print(sys.path)

from utils.message_formatter import format_news_message
from pyrogram import Client
from services.mongodb_service import db
from utils.log_utils import setup_logging
from typing import List

logger = setup_logging()

class NewsPosterService:
    def __init__(self, app: Client, news_fetcher):
        self.app = app
        self.news_fetcher = news_fetcher
        
    async def fetch_and_post_news(self, chat_id):
        try:
            # Fetch the latest articles using the scraper service
            latest_articles = await self.news_fetcher.fetch_latest_news()
            
            if not latest_articles:
                logger.info("No new articles found to post.")
                return
            
            for article in latest_articles:
                formatted_message = format_news_message({
                    "title": article['title'],
                    "content": article['content'],
                    "link": article['link']
                })
                # Post each formatted news message to the specified Telegram chat
                await self.app.send_message(chat_id, formatted_message)
                logger.info(f"Posted article '{article['title']}' to chat {chat_id}.")
        
        except Exception as e:
            logger.error(f"Error fetching or posting news: {e}", exc_info=True)

    async def fetch_latest_news_from_mongo(self) -> List[str]:
        try:
            latest_articles = await db.find().sort("timestamp", -1).to_list(length=1)
            if not latest_articles:
                return []
            
            formatted_articles = [
                format_news_message({
                    "title": article['title'],
                    "content": article['content'],
                    "link": article['link']
                })
                for article in latest_articles
            ]
            return formatted_articles

        except Exception as e:
            logger.error(f"Error fetching news from MongoDB: {e}", exc_info=True)
            return []
