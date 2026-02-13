rag-chatbot/
│
├── app/
│   ├── main.py
│   ├── api/
│   │   ├── documents.py
│   │   ├── chat.py
│   │   └── auth.py
│   ├── core/
│   │   ├── config.py
│   │   └── celery_app.py
│   ├── services/
│   │   ├── ingestion.py
│   │   ├── rag.py
│   │   └── embeddings.py
│   ├── db/
│   │   ├── models.py
│   │   └── session.py
│   ├── vectorstore/
│   │   └── chroma.py
│   └── schemas/
│       └── schemas.py
│
├── worker.py
├── requirements.txt
├── README.md
└── .env

