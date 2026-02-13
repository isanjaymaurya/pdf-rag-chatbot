from celery import Celery

Celery = Celery(
    'worker',
    broker='redis://locahost:6379/0',
    backend='redis://locahost:6379/0'
)