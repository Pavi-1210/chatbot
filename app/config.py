import os

class Config(object):
    # HUGGINGFACEHUB_API_TOKEN = os.environ.get('HUGGINGFACEHUB_API_TOKEN') or 'you-will-never-guess'
    COHERE_API_KEY = os.environ.get('COHERE_API_KEY') or 'you-will-never-guess'
    GOOGLE_API_KEY=os.environ.get('GOOGLE_API_KEY') or 'you-will-never-guess'
    # Add other configuration variables here
