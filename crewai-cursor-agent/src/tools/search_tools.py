from langchain.tools import BaseTool
from duckduckgo_search import DDGS


class SearchTools:
    @staticmethod
    def web_search() -> BaseTool:
        def search(query: str, max_results: int = 5) -> str:
            """Perform a web search using DuckDuckGo"""
            try:
                with DDGS() as ddgs:
                    results = list(ddgs.text(query, max_results=max_results))
                    formatted_results = []
                    for r in results:
                        formatted_results.append(
                            f"Title: {r['title']}\nLink: {r['link']}\nSnippet: {r['body']}\n"
                        )
                    return "\n---\n".join(formatted_results)
            except Exception as e:
                return f"Error performing web search: {str(e)}"

        return BaseTool(
            name="Web Search",
            func=search,
            description="Searches the web using DuckDuckGo for relevant information"
        )
