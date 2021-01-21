from celery import Celery
from celery.schedules import crontab # scheduler
import requests
from bs4 import BeautifulSoup  # xml parsing
import json
from datetime import datetime

app = Celery('tasks')  # defining the app name to be used in our flag

# scheduled task execution
app.conf.beat_schedule = {
    # executes every 1 minute
    'scraping-task-one-min': {
        'task': 'tasks.get_rss',
        'schedule': crontab()
    }
}

# South China Morning Post - China Tech RSS feed


@app.task
def save_function(article_list):

    timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
    filename = 'articles-{}.json'.format(timestamp)

    # creating the articles file with timestamp
    with open(filename, 'w') as outfile:
        json.dump(article_list, outfile)


# scraping function
@app.task
def get_rss():

    article_list = []
    try:
        r = requests.get('https://www.scmp.com/rss/320663/feed')

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
                'published': published,
                'created_at': str(datetime.now()),
                'source': 'RSS feed'
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
