from prompt_generator.professions import Professions 
from prompt_generator.utils import completions

class PromptGenerator:

    def __init__(self):
        self.gpt_completions = completions.GPTCompletions()

    #  use prompt design to generate a structured response
    def generate_professions(self, num_professions:int, profession_list=None):
        prompt = Professions.generate_professions(num_professions, profession_list)
        completion = self.gpt_completions.gpt_response(prompt)

        return completion.message.content


# if __name__ == '__main__':
#     prompt_generator = PromptGenerator()
#     professions = prompt_generator.generate_professions(['Doctor', 'Boxer', 'Astronaut'])
#     print(professions)
