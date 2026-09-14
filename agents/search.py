from tavily import TavilyClient
import os

tavily_key = os.getenv("TAVILY_API_KEY")
tavily_client = TavilyClient(api_key=tavily_key) if tavily_key else None


class SearchAgent:
    def __init__(self):
        pass

    def search_tavily(self, query: str):
        if not tavily_client:
            return [{"title": "Search Fallback", "content": f"TAVILY_API_KEY not configured. Query: {query}", "url": "https://example.com"}], "https://images.unsplash.com/photo-1542281286-9e0a16bb7366"
        results = tavily_client.search(query=query, topic="news", max_results=10, include_images=True)
        sources = results["results"]
        try:
            image = results["images"][0]
        except:
            image = "https://images.unsplash.com/photo-1542281286-9e0a16bb7366?ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8bmV3c3BhcGVyJTIwbmV3c3BhcGVyJTIwYXJ0aWNsZXxlbnwwfHwwfHw%3D&ixlib=rb-1.2.1&w=1000&q=80"
        return sources, image

    def run(self, article: dict):
        res = self.search_tavily(article["query"])
        article["sources"] = res[0]
        article["image"] = res[1]
        return article
