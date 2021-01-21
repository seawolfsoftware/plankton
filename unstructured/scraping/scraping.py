import json
import requests
from bs4 import BeautifulSoup



# scraping function
def get_rss(endpoint):

    # South China Morning Post - China Tech RSS feed
    endpoint = 'https://www.scmp.com/rss/320663/feed'

    article_list = []
    try:
        r = requests.get(endpoint)

        # parse the data using the XML parser in bs4
        soup = BeautifulSoup(r.content, features='xml')

        # select the "items" wanted from the data
        articles = soup.findAll('item')

        # for each "item", parse it into a list
        for a in articles:
            title = a.find('title').text
            link = a.find('link').text
            published = a.find('pubDate').text

            # create an "article" object with the data
            # from each "item"
            article = {
                'title': title,
                'link': link,
                'published': published
                }

            # append "article_list" with each "article" object
            article_list.append(article)

        for a in article_list:
            print(a)
        # after the loop, dump the saved objects into a .txt file
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