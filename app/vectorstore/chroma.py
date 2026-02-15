from langchain_chroma import Chroma
from langchain_ollama import ChatOllama
from langchain_ollama import OllamaEmbeddings
from langchain_classic.chains.retrieval_qa.base import RetrievalQA

llm = ChatOllama(model="mistral")
embeddings = OllamaEmbeddings(model="nomic-embed-text")

# Load vector DB
vectorstore = Chroma(persist_directory="./chroma", embedding_function=embeddings)
# Create RAG pipeline
qa = RetrievalQA.from_chain_type(llm=llm, retriever=vectorstore.as_retriever())

print(qa.invoke("What is this document about?"))
