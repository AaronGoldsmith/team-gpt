# Test that our connection to OpenAI works
import os
import openai
from dotenv import load_dotenv

# load in env file from root
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

# Initial test to check that our API key is loaded from the root .env file 
def test_openai_connection():
    api_key = os.getenv("OPENAI_API_KEY")
    openai.api_key = api_key
    models = openai.Model.list()
    assert len(models["data"]) > 0, "API call failed: invalid or missing API key"
 