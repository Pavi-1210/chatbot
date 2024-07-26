from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

import os
from dotenv import load_dotenv

load_dotenv()

# os.environ['HUGGINGFACEHUB_API_TOKEN'] = os.getenv('HUGGINGFACEHUB_API_TOKEN')
os.environ['COHERE_API_KEY'] = os.getenv('COHERE_API_KEY')
os.environ["GOOGLE_API_KEY"]=os.getenv('GOOGLE_API_KEY')
os.environ["PINECONE_API_KEY"]=os.getenv('PINECONE_API_KEY')

from app.routes import *
