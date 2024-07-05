import openai

from config.index import OPENAI_KEY

# Set up your OpenAI API key
openai.api_key = OPENAI_KEY
def connect_open_ai():
    return openai
