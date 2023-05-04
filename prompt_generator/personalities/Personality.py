import json
from .default_traits import DEFAULT_TRAITS
from prompt_generator.PromptGenerator import PromptGenerator

# create an instance of PromptGenerator
PromptGenerator = PromptGenerator()
custom_traits_path = "custom_traits.json"

class Personality:
    # attempt to load in custom traits
    @classmethod
    def load_custom_traits(self):
        try:
            with open(custom_traits_path, "r") as file:
                self.CUSTOM_TRAITS = json.load(file)
        except FileNotFoundError:
            pass

    # required traits first, and custom/optional at the end
    def __init__(self, extraversion: int, agreeableness: int, **kwargs):
        self.traits = {
            "extraversion": extraversion,
            "agreeableness": agreeableness
        }
        self.DEFAULT_TRAITS = DEFAULT_TRAITS
        self.CUSTOM_TRAITS = {}
        # load from file
        self.load_custom_traits()
        # add new traits
        self.add_custom_traits(kwargs)
        # merge with class traits
        self.traits.update(kwargs)

    # takes a list of traits, and assigns descriptions from GPT
    def add_custom_traits(self, traits):
        for trait in traits:
            if trait not in self.DEFAULT_TRAITS and trait not in self.CUSTOM_TRAITS:
                description = PromptGenerator.get_trait_description(trait)
                self.CUSTOM_TRAITS[trait] = json.loads(description)[trait]
                self.save_custom_traits()

    def save_custom_traits(self):
        try:
            with open(custom_traits_path, "r") as file:
                existing_traits = json.load(file)
        except FileNotFoundError:
            existing_traits = {}
        
        with open(custom_traits_path, "w") as file:
            # combine existing and new traits
            custom_traits = {**existing_traits, **self.CUSTOM_TRAITS}
            json.dump(custom_traits, file, indent=2)
            

Personality.load_custom_traits()

