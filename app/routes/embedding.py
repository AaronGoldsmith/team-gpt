import openai
import os
from fastapi import APIRouter, Query
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
router = APIRouter()

@router.get("/generate/")
def create_embedding(text: str = Query(None)):
    if not text: return "No text"
    # Embedding creation logic goes here
    response = openai.Embedding.create(
      input=text,
      model="text-embedding-ada-002"
    )
    embeddings = response['data'][0]['embedding']
    return embeddings