from celery import Celery
from app.core.config import settings

Celery = Celery(
    'worker',
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL
)