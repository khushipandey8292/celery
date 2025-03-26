import os
from celery import Celery
from time import sleep

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myceleryproject.settings')

app = Celery('myceleryproject')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


# @app.task
# def sub(x,y):
#     sleep(20)
#     return x-y