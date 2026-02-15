from app.worker import celery
from app.services.ingestion import process_document

@celery.task
def process_document_task(filename: str):
    return process_document(filename)
