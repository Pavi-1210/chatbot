import os
import re
import time
from langchain_community.embeddings import HuggingFaceEmbeddings
# from langchain_community.vectorstores import Chroma
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone , ServerlessSpec
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))


pdf_vectordb = None
persist_directory = 'db/pdf_vector_db'
sanitized_video_name = re.sub(r'[^a-z0-9\-]', '-', persist_directory.lower())
persist_directory = sanitized_video_name
existing_indexes = [index_info["name"] for index_info in pc.list_indexes()]

if persist_directory not in existing_indexes:
        pc.create_index(
        name=persist_directory,
        dimension=768,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1"),
    )
while not pc.describe_index(persist_directory).status["ready"]:
        time.sleep(1)
index = pc.Index(persist_directory)
embedding = HuggingFaceEmbeddings()

def embed(text):
    global pdf_vectordb
    pdf_vectordb = PineconeVectorStore.from_documents(text,
                                         embedding,
                                         index_name=persist_directory)
    pdf_vectordb.persist()
    pdf_vectordb = None
    pdf_vectordb = PineconeVectorStore(index_name=persist_directory,
                          embedding=embedding)
    return "done"

pdf_vectordb = PineconeVectorStore(index_name=persist_directory,
                      embedding=embedding)

print("Vector_db loaded")
