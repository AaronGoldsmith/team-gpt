from dotenv import load_dotenv
from fastapi import FastAPI
from api.v1.endpoints import router as api_router
# import os
load_dotenv('../.env')

# Initialize FastAPI application

app = FastAPI()

# openai.api_key = os.getenv("OPENAI_API_KEY")
app.include_router(api_router, prefix="/api/v1")
print(app.routes)

