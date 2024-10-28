#interfaces/news_fetcher_interface.py

from abc import ABC, abstractmethod
from typing import List, Dict

class NewsFetcherInterface(ABC):
    
    @abstractmethod
    async def fetch_latest_news(self) -> List[Dict[str, str]]:
        """Fetches the latest news articles."""
        pass
