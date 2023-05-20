from dotenv import load_dotenv

import os
import pinecone
load_dotenv(os.path.join(os.path.dirname(__file__), '..','..', '.env'))
pinecone_api_key = os.getenv("PINECONE_API_KEY")
if pinecone_api_key is None:
    raise ValueError("PINECONE_API_KEY environment variable is not set")

# Get the Pinecone API environment
pinecone_api_env = os.getenv("PINECONE_API_ENV")
if pinecone_api_env is None:
    pinecone_api_env = "us-west-4"  # Set a default value if the variable is not set

# Initialize Pinecone
pinecone.init(api_key=pinecone_api_key, environment=pinecone_api_env)

index_name = 'langchain-retrieval-agent'

     # we create a new index
pinecone.create_index(
    name='langchain-retrieval-agent',
    metric='dotproduct',
    dimension=1536  # 1536 dim of text-embedding-ada-002
 )

   
