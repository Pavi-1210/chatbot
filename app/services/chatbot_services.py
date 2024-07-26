import sqlite3 as sql
from langchain_community.llms import Cohere
from langchain_core.runnables import RunnablePassthrough
from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_core.output_parsers import StrOutputParser
from app.services.prompt import *
# Load environment variables and initialize the model
import os
from dotenv import load_dotenv
from app.services.retreiver import *

load_dotenv()
# os.environ['HUGGINGFACEHUB_API_TOKEN'] = os.getenv("HUGGINGFACEHUB_API_TOKEN")
os.environ['COHERE_API_KEY'] = os.getenv("COHERE_API_KEY")
os.environ['GOOGLE_API_KEY']=os.getenv("GOOGLE_API_KEY")
# model = Cohere(model="command", temperature=1)
model = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0.5)


def handle_question(question):
    chain = (
        {"context": pdf_retriever, "question": RunnablePassthrough()}
        | prompt
        | model
        | StrOutputParser()
    )

    answer = chain.invoke(question)
    # if "couldn't understand" in answer:
    #     print("pdf")
    #     chain = (
    #         {"context": pdf_retriever, "question": RunnablePassthrough()}
    #         | prompt
    #         | model
    #         | StrOutputParser()
    #     )
    #     answer = chain.invoke(question)
    # else:
    #     print("csv")
    return answer

# def handle_similar_queries(query):
#     docs = csv_retriever.get_relevant_documents(query)
#     prompts = extract_prompts(docs)
#     return list(prompts)


# def extract_prompts(documents):
#     unique_prompts = set()
#     for doc in documents:
#         if 'PROMPT' in doc.page_content:
#             prompt_text = doc.page_content.split(':')[1].strip()
#             prompt_text = prompt_text.split('\n')[0] 
#             unique_prompts.add(prompt_text)
#     return unique_prompts
