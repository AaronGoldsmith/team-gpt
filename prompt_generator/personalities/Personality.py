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
                cls.custom_traits = json.load(file)
        except FileNotFoundError:
            pass

    # required traits first, and custom/optional at the end
    def __init__(self, extraversion: int, agreeableness: int, custom_traits_path=None, saved_traits={}, **kwargs):
        self.traits = {
            "extraversion": extraversion,
            "agreeableness": agreeableness
        }
        self.custom_traits_path = (custom_traits_path or Personality.custom_traits_path)
        self.custom_traits = saved_traits
        self.load_custom_traits()
        self.add_custom_traits(kwargs)
        self.traits.update(kwargs)

        self.trait_defs = {k: v for k, v in DEFAULT_TRAITS.items() if k in self.traits}



        
    def add_custom_traits(self, traits):
        """
        Takes a list of traits, and assigns descriptions from GPT
        """
        for trait in traits:
            if trait not in DEFAULT_TRAITS and trait not in self.custom_traits:
                description = Personality.prompt_generator.get_trait_description(trait)
                self.custom_traits[trait] = json.loads(description)[trait]
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
            custom_traits = {**existing_traits, **self.custom_traits}
            json.dump(custom_traits, file, indent=2)
    

    def save_personality(personality, filename):
        """
        Save personality to a file
        """
        with open(filename, 'w') as f:
            json.dump(personality.__dict__, f)

    def load_personality(filename):
        """
        Load personality from a file
        """
        with open(filename, 'r') as f:
            personality_data = json.load(f)
        d = personality_data['custom_traits']

        return Personality( **personality_data['traits'], saved_traits=personality_data["custom_traits"])

# Load custom traits at module level
Personality.load_custom_traits()
