from fastapi import APIRouter
from api.v1.pinecone_routes import router as pinecone_router
from routes.embedding import router as embed_router

router = APIRouter()

router.include_router(pinecone_router, prefix="/embeddings", tags=["embeddings"])
router.include_router(embed_router, prefix="/embeddings", tags=["embeddings"])
