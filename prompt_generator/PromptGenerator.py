import openai
import os

from dotenv import load_dotenv
import Professions 

class PromptGenerator:

  def __init__(self):
      # Load API key from environment variables
      load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))
      openai.api_key = os.getenv("OPENAI_API_KEY")

  def generate_professions(self, num_professions, professions=["None provided"]):
      prompt = Professions.generate_professions(num_professions, professions)
    
      #  use prompt engineering to generate a structured response
      completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
      )

      return completion.choices[0].message.content

if __name__ == '__main__':
    prompt_generator = PromptGenerator()
    professions = prompt_generator.generate_professions(2, ['Doctor','Sushi Chef','Chocolatier','Construction Worker','Model','Product Manager'])
    print(professions)


