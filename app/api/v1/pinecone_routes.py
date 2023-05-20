from fastapi import APIRouter
from services.PineconeService import PineconeService
from typing import List, Tuple
import pinecone

router = APIRouter()

@router.post("/upsert")
def upsert_data(data: List[Tuple[str, List[float]]]):
    index = pinecone.Index("my-index")
    index.upsert(items=data)
    return {"message": "Upsert successful"}

@router.post("/query")
def query_data(query: List[float], top_k: int):
    index = pinecone.Index("my-index")
    results = index.query(queries=[query], top_k=top_k)
    return results

@router.post("/")
def query_data():
  return {"text": "hello world"}
