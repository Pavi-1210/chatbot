from langchain_community.document_loaders import CSVLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from .embedding import embed  # Correctly import the embed function

import pdfplumber

# Function to extract text from PDF using pdfplumber
def extract_text(file_path):
    text = ''
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + '\n'
    return text

def extract_text_from_pdf(file):
    document = extract_text(file)
    docs = Document(page_content=document)
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    text = text_splitter.split_documents([docs])
    embed(text)  # Use the embed function
    return document



