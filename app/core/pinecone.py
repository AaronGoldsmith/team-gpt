
import os
import pinecone

# Initialize Pinecone
pinecone_api_key = os.getenv("PINECONE_API_KEY")
pinecone_api_env = os.getenv("PINECONE_API_ENV")

pinecone.init(api_key=pinecone_api_key, environment=pinecone_api_env)


def create_index(index_name):
  indexes = pinecone.list_indexes()
  try:
    indexes.index(index_name)
  except ValueError:
    pinecone.create_index(index_name, dimension=8, metric='euclidean')    

def list_indexes():
  indexes = pinecone.list_indexes()
  return indexes;