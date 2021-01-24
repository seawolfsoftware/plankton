from __future__ import absolute_import
import os
from celery import Celery
from celery.schedules import crontab


# default django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'plankton.settings')
# app = Celery('plankton')
# app.conf.timezone = 'UTC'
# app.config_from_object("django.conf:settings", namespace="CELERY")
# app.autodiscover_tasks()
#
# app.conf.beat_schedule = {
#     # executes every 1 minute
#     'scraping-task-one-min': {
#         'task': 'scraping.tasks.get_rss',
#         'schedule': crontab(),
#     }
#     # # executes every 15 minutes
#     # 'scraping-task-fifteen-min': {
#     #     'task': 'tasks.hackernews_rss',
#     #     'schedule': crontab(minute='*/15')
#     # },
#     # # executes daily at midnight
#     # 'scraping-task-midnight-daily': {
#     #     'task': 'tasks.hackernews_rss',
#     #     'schedule': crontab(minute=0, hour=0)
#     # }
# }

app2 = Celery('plankton')
app2.conf.timezone = 'UTC'
app2.config_from_object("django.conf:settings", namespace="CELERY")
app2.autodiscover_tasks()
args = ["test"]
app2.conf.beat_schedule = {
    # executes every 1 minute
    'headlines-task-one-min': {
        'task': 'headlines.tasks.search_headlines',
        'schedule': crontab(),
        'args': args,
    }
}