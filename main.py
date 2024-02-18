from transformers import pipeline
from search import searchIt
from scrape import scrape
import os
import json
from math import floor
from further import furtherSearch
from getImages import getImages

def json_output(query: str, summary:str, relatedArticles:list, keywords:list, imageLinks:list):
    output = {
        "input": f"{query}",
        "summary": f"{summary}",
        "sources":relatedArticles,
        "keywords": keywords,
        "imageLinks": imageLinks
    }

    return json.dumps(output, indent=4)

def fetchoutput(query:str):
    # os.system("clear")
    # query = input("enter the query: ")
    article_urls = searchIt(query)
    text = scrape(article_urls)
    
    # model selection as per sequence length: {t5-small: 512, bart: 1024}
    if len(text) <= 512:
        model = "t5-small"
    else:
        model = "facebook/bart-large-cnn"
        text = text[:floor(1024*2.9)]

    # customise length and summarise:
    # customise = input("wish to customise the model[Y/N]: ").lower()
    customise = 'n'
    if customise == "y":
        max = input("Max length: ")
        min = input("Min Length: ")
        summariser = pipeline("summarization", model=model)
        summary = summariser(text, max_length=max, min_length=min, do_sample=False)[0]['summary_text']
    else:
        summariser = pipeline("summarization", model=model)
        summary = summariser(text, max_length=250, min_length=50, do_sample=False)[0]['summary_text']
    
    keywords = furtherSearch(text)['keywords']
    images = getImages(query)

    # the JSON output object here:
    output = json_output(query, summary, article_urls, keywords=keywords, imageLinks=images)
    return output
    # print("\n")
    # print(summary)
    # print("\n")
    # for i in range(len(article_urls)):
    #     print(article_urls[i])
    # print("\n")

    # print(output)

# if __name__ == "__main__":
#     main()

