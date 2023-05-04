import json
from .default_traits import DEFAULT_TRAITS
from prompt_generator.PromptGenerator import PromptGenerator

class Personality:

    # Create an instance of PromptGenerator
    prompt_generator = PromptGenerator()
    custom_traits_path = "custom_traits.json"

    @classmethod
    def load_custom_traits(cls):
        """
        Attempt to load in custom traits
        """
        try:
            with open(cls.custom_traits_path, "r") as file:
                cls.CUSTOM_TRAITS = json.load(file)
        except FileNotFoundError:
            pass

    # required traits first, and custom/optional at the end
    def __init__(self, extraversion: int, agreeableness: int, custom_traits_path=None, **kwargs):
        self.traits = {
            "extraversion": extraversion,
            "agreeableness": agreeableness
        }
        self.custom_traits_path = custom_traits_path or Personality.custom_traits_path
        self.DEFAULT_TRAITS = DEFAULT_TRAITS
        self.CUSTOM_TRAITS = {}
        self.load_custom_traits()
        self.add_custom_traits(kwargs)
        self.traits.update(kwargs)

        
    def add_custom_traits(self, traits):
        """
        Takes a list of traits, and assigns descriptions from GPT
        """
        for trait in traits:
            if trait not in self.DEFAULT_TRAITS and trait not in self.CUSTOM_TRAITS:
                description = Personality.prompt_generator.get_trait_description(trait)
                self.CUSTOM_TRAITS[trait] = json.loads(description)[trait]
                self.save_custom_traits()

    def save_custom_traits(self):
        """
        Save custom traits to a file
        """
        try:
            with open(self.custom_traits_path, "r") as file:
                existing_traits = json.load(file)
        except FileNotFoundError:
            existing_traits = {}
        with open(self.custom_traits_path, "w") as file:
            custom_traits = {**existing_traits, **self.CUSTOM_TRAITS}
            json.dump(custom_traits, file, indent=2)
            

# Load custom traits at module level
Personality.load_custom_traits()
