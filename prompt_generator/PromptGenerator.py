
from .utils.GPTCompletions import GPTCompletions
from .professions import Professions
from .personalities.trait_description import generate_trait_description


class PromptGenerator:

    def __init__(self):
        self.gpt_completions = GPTCompletions()

    #  use prompt design to generate a structured response
    def generate_professions(self, num_professions:int, profession_list=None):
        prompt = Professions.generate_professions(num_professions, profession_list)
        completion = self.gpt_completions.gpt_response(prompt)

        return completion.message.content

    def get_trait_description(self, trait):
        prompt = generate_trait_description(trait)
        completion = self.gpt_completions.gpt_response(prompt)

        return completion.message.content



