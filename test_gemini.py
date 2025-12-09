
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("LLM_API_KEY")
base_url = os.getenv("LLM_BASE_URL", "https://generativelanguage.googleapis.com/v1beta/openai/")

print(f"Testing with Base URL: {base_url}")
print(f"Model: {os.getenv('MODEL_NAME')}")

client = OpenAI(
    api_key=api_key,
    base_url=base_url,
)


print("\nListing available models:")
try:
    models = client.models.list()
    for m in models.data:
        print(f"- {m.id}")
except Exception as e:
    print(f"Failed to list models: {e}")
