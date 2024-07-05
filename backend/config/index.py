import os

from dotenv import load_dotenv

load_dotenv()

ENVIRONMENT = os.getenv("ENVIRONMENT")
APP_NAME = os.getenv("APP_NAME")
PORT = os.getenv("PORT")
OPENAI_KEY = os.getenv("OPENAI_KEY")
