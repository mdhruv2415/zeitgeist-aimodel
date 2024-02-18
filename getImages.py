# to take the query and search for top three images via News API
from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key="d607cfb6599e4cf8a7c050223a27c10e")

def getImages(query:str):
    all_articles = newsapi.get_everything(q=query,
                                        sources="the-hindu,the-times-of-india,google-news-in", 
                                        language='en',
                                        sort_by='relevancy',
                                        page_size=3,
                                        page=1)
    # saving the top three articles' URLs:
    imageLinks = []
    for i in range(len(all_articles['articles'])):
        imageLinks.append(all_articles['articles'][i]['urlToImage'])
    return imageLinks if (len(all_articles['articles']) < 3) else imageLinks[:3]