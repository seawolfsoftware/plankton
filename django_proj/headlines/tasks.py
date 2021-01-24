import json
import os
import requests
from celery import shared_task
from celery.utils.log import get_task_logger

from .curations import Curation
from .models import Headline

logger = get_task_logger(__name__)


@shared_task(serializer='json')
def save_function(headline_list):
    """Save headlines to the database.
    Saves headlines to the database if they do not already exist.
    Parameters:
        headline_list (json, str): A JSON list of headline objects.
    Returns:
        Headline (class Headline): Headline objects for each unique article.
    """
    new_count = 0

    error = True
    try:
        print('THIS IS RUNNING')
        latest_headline = Headline.objects.all()
        print(latest_headline.published)
        print('var TestTest: ', latest_headline, 'type: ', type(latest_headline))
    except Exception as e:
        print('Exception at latest_headline: ')
        print(e)
        error = False
        pass
    finally:
        # if the latest_headline has an index out of range (nothing in model) it will fail
        # this catches failure so it passes the first if statement

        if error is not True:
            latest_headline = None

    for headline in headline_list:

        # latest_headline is None signifies empty DB
        if latest_headline is None:
            try:
                Headline.objects.create(
                    title="test"
                )
                new_count += 1
            except Exception as e:
                print('failed at latest_headline is none')
                print(e)
                break

        # latest_headline.published date < headline['published']
        # halts the save, to avoid repetitive DB calls on already existing headlines
        elif latest_headline.published < headline['published']:
            try:
                Headline.objects.create(
                    title="test",
                )
                new_count += 1
            except:
                print('failed at latest_headline.published < j[published]')
                break
        else:
            return print('headline scraping failed')

    logger.info(f'New headlines: {new_count} headline(s) added.')
    return print('finished')


@shared_task
def search_headlines(queryString):

    api_key = os.environ.get("FT_API_KEY")

    headers = {
      "X-Api-Key": "{}".format(api_key),
      "Content-Type": "application/json"
    }

    endpoint = "https://api.ft.com/content/search/v1?"

    payload = {
        "queryString": queryString,
        "queryContext": {
             "curations": [Curation.Articles, Curation.Pages]
        }
    }

    response = requests.post(
        endpoint,
        headers=headers,
        json=payload
    )
    print(response.json())
    headlines = ''
    return save_function(headlines)


# main.py
queryString = "title:\"johnson & johnson\""
headlines = search_headlines(queryString)

# the list of queries to be performed every 24 hours
queryStrings = []
