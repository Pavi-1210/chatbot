from app.services.embedding import *

pdf_retriever = pdf_vectordb.as_retriever(search_kwargs={"k": 3})


# csv_retriever = csv_vectordb.as_retriever(search_kwargs={"k": 3})
