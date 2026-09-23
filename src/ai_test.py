import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI()

response = client.responses.create(
    model="gpt-5.6-luna",
    input="Explica qué es una API en una sola oración."
)

print(response.output_text)