import os
import json
from prompt_generator.personalities.Personality import Personality

class TestPersonality:

    def setup_method(self):
        self.default_traits = {"extraversion": 7, "agreeableness": 6}
        self.custom_traits = {"happiness": 4}

    def teardown_method(self):
        if os.path.exists("custom_traits.json"):
            os.remove("custom_traits.json")

    def test_default_traits(self):
        personality = Personality(extraversion=7, agreeableness=6)
        assert self.default_traits == {k: v for k, v in personality.traits.items() if k in self.default_traits}

    def test_add_custom_traits(self):
        personality = Personality(extraversion=7, agreeableness=6, **self.custom_traits)
        assert all(trait in personality.CUSTOM_TRAITS for trait in self.custom_traits)
        assert os.path.exists("custom_traits.json")

        with open("custom_traits.json", "r") as file:
            saved_custom_traits = json.load(file)

        assert all(trait in saved_custom_traits for trait in self.custom_traits)

    # test if our custom traits are added and are assigned descriptions
    def test_load_custom_traits(self):
        personality = Personality(extraversion=7, agreeableness=6, **self.custom_traits)
        personality2 = Personality(extraversion=5, agreeableness=4)
        saved_traits = {}
        with open("custom_traits.json", "r") as file:
            saved_traits = json.load(file)
        for trait in self.custom_traits:
            assert trait in saved_traits