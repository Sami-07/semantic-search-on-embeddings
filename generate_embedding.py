import requests
import os
from dotenv import load_dotenv

load_dotenv()

EMBEDDING_URL = "https://api-inference.huggingface.co/pipeline/feature-extraction/sentence-transformers/all-MiniLM-L6-v2"

def generate_embedding(text: str) -> list[float]:
    response = requests.post(EMBEDDING_URL, headers={
                             "Authorization": f"Bearer {os.getenv('HUGGING_FACE_TOKEN')}"}, json={"inputs": text})
    if (response.status_code != 200):
        raise ValueError(
            f"Request failed with status code {response.status_code}: {response.text}")
    return response.json()

# Export the function
__all__ = ['generate_embedding']