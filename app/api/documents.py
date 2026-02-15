from fastapi import APIRouter, UploadFile
from app.core.celery_app import process_document_task

router = APIRouter()

@router.post("/upload")
async def upload_document(file: UploadFile):
    task = process_document_task.delay(file.filename)
    return {"task_id": task.id}


