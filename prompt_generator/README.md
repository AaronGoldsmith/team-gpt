# Prompt Generator

This module uses OpenAI's GPT-3.5-turbo to generate a JSON-formatted string containing a list of distinct professions along with their skills and expertise. The goal of this module is to create a basic framework for creating artificial professional teams. 

## Features

- Generate a [list of professions](#generate-professions) with their skills and expertise. 
- Generate a [definition for new Personality traits](#generate-trait-definitions)
- Customize the number of professions in the generated list
- Provide a list of preferred professions to include in the generated response
- Get a JSON-formatted string containing the profession details


## Usage


### Generate Professions
```python
prompt_generator = PromptGenerator()
prompt_generator.generate_professions(2,['Doctor', 'Boxer', 'Astronaut'])
```

Example output
```bash
{
  "professions": [
    {
      "name": "Doctor",
      "known_for": "Treating illnesses and injuries, prescribing medication",
      "lesser_known_for": "The importance of preventative care and public health initiatives",
      "contribution": "A doctor could provide medical expertise and advice on potential health risks and safety precautions for a cross-functional team project"
    },
    {
      "name": "Boxer",
      "known_for": "Fighting opponents in a regulated sport",
      "lesser_known_for": "The discipline and rigorous training required to compete at a high level",
      "contribution": "A boxer could bring a strong work ethic and determination to a cross-functional team project, as well as providing insights on physical training and conditioning" 
    }
  ]
}
```

### Generate Trait Definitions

```python
generator = PromptGenerator()
description = generator.get_trait_description('Shy')
```