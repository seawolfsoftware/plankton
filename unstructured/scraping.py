import json
import requests
from bs4 import BeautifulSoup


# South China Morning Post - China Tech RSS feed
endpoint = 'https://www.scmp.com/rss/320663/feed'


# scraping function
def get_rss(endpoint):
    article_list = []
    try:
        r = requests.get(endpoint)
        soup = BeautifulSoup(r.content, features='xml')
        articles = soup.findAll('item')
        for a in articles:
            title = a.find('title').text
            link = a.find('link').text
            published = a.find('pubDate').text
            article = {
                'title': title,
                'link': link,
                'published': published
                }
            article_list.append(article)

        for a in article_list:
            print(a)
        return save_function(article_list)

    except Exception as e:
        print('The scraping job failed. See exception: ')
        print(e)


def save_function(article_list):
    with open('articles.txt', 'w') as outfile:
        json.dump(article_list, outfile)

print('Starting scraping')

get_rss(endpoint)

print('Finished scraping')