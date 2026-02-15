import uvicorn
from fastapi import FastAPI
from app.api import documents

app = FastAPI()

app.include_router(documents.router, prefix="/documents", tags=["documents"])


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
