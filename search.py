import os
from langchain.tools import Tool
from langchain.utilities import GoogleSearchAPIWrapper

os.environ["GOOGLE_CSE_ID"] = "270e6df931d77417f"
os.environ["GOOGLE_API_KEY"] = "AIzaSyBEhk8TuIU6etLQJXRsj-iLJPMBAX5FYSw"

search = GoogleSearchAPIWrapper()

def top_5_results(query):
    return search.results(query, 5)

def searchIt(query:str):
    tool = Tool(
        name="Google Search Snippets",
        description="Search Google for recent results.",
        func=top_5_results,
    )

    restricted_sites = "-site:youtube.com -site:nytimes.com -site:wsj.com"

    return [tool.run(f"{query} {restricted_sites}")[i]['link'] for i in range(3)]