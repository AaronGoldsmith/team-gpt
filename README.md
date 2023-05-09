# Team GPT


Create a team of reusable GPT agents with specialities and personalities

Personalities are made up of a dictionary of traits which map to a numeric weight. These values are used to influence the tone and reasoning of the LLM.  
- The Personality class **requires** a score for extraversion and agreeableness. 
- The Personality class can accept new traits at runtime. Trait definitions are provided by OpenAI GPT 3.5-turbo



## Installation
`pip install -r requirements.txt`


## Architecture 

### [Prompt Generator](./prompt_generator/README.md)
### [Personality](./prompt_generator/personalities/README.md)

### [Testing](./tests/README.md)




