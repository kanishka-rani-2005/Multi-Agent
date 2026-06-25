from src.tools.tools import web_search,scrape_url
from src.pipeline.pipeline import run_research_pipeline


# result=scrape_url.invoke({"url": "https://old.reddit.com/r/artificial"})
# print(result)


result = run_research_pipeline("Artificial Intelligence")
print("\n\n\n Final Research Report : \n",result['report'])