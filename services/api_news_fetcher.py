#services/api_news_fetcher.py
#Purpose: For other news api endpoint to interact other than cointelegraph 

from interfaces.news_fetcher_interface import NewsFetcherInterface
import requests
from typing import List, Dict
#from utils.message_formatter import format_news_message  # Import the formatting utility

class APINewsFetcher(NewsFetcherInterface):
    
    def __init__(self, api_url: str):
        self.api_url = api_url
    
    async def fetch_latest_news(self) -> List[Dict[str, str]]:
        response = requests.get(self.api_url)
        articles = response.json()  # Assuming the API returns a list of articles

        # Use format_news_message for consistent formatting
        formatted_articles = [
            format_news_message({
                "title": article["title"],
                "content": article["content"],
                "link": article["url"]
            })
            for article in articles
        ]
        return formatted_articles
