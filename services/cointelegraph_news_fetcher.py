#services/cointelegraph_news_fetcher.py
import sys
sys.path.insert(0, '/root/folder/cointelegraph_news_scraper')

from interfaces.news_fetcher_interface import NewsFetcherInterface
from cointelegraph_news_scraper.services.scraper_service import collect_articles
from typing import List, Dict

class CointelegraphNewsFetcher(NewsFetcherInterface):
    
    async def fetch_latest_news(self) -> List[Dict[str, str]]:
        articles = await collect_articles()
        formatted_articles = [
            {"title": article["title"], "content": article["content"], "link": article["link"]}
            for article in articles
        ]
        return formatted_articles
