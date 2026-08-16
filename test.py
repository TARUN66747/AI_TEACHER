import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client()

# List all supported model names
for model in client.models.list():
    if "generateContent" in model.supported_actions:
        print(model.name)