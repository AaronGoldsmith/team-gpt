import os
import json

from prompt_generator.personalities.Personality import Personality

class TestPersonality:

    def setup_method(self):
        # use temp file as to not delete our existing traits
        self.default_traits = {"extraversion": 7, "agreeableness": 6}
        self.custom_traits = {"happiness": 4}
        self.temp_file = "tests/custom_test_traits.json"

    # delete the test file using a Class fixture
    def teardown_method(self):
        if os.path.exists(self.temp_file):
            os.remove(self.temp_file)

    def test_default_traits(self):
        personality = Personality(extraversion=7, agreeableness=6)
        assert self.default_traits == {k: v for k, v in personality.traits.items() if k in self.default_traits}

    def test_add_custom_traits(self):
        personality = Personality(extraversion=7, agreeableness=6, custom_traits_path=self.temp_file, **self.custom_traits)
        assert all(trait in personality.custom_traits for trait in self.custom_traits)
        assert os.path.exists(self.temp_file)
        with open(self.temp_file, "r") as file:
            try:
                saved_custom_traits = json.load(file)
            except json.JSONDecodeError:
                saved_custom_traits = {}
        assert all(trait in saved_custom_traits for trait in self.custom_traits)

    # test if our custom traits are added and are assigned descriptions
    def test_load_custom_traits(self):
        Personality(extraversion=7, agreeableness=6, challenger=3, custom_traits_path=self.temp_file, **self.custom_traits)
        saved_traits = {}
        with open(self.temp_file, "r") as file:
            try:
                saved_traits = json.load(file)
            except json.JSONDecodeError:
                saved_traits = {}

        for trait in self.custom_traits:
            assert trait in saved_traits
    
    def test_save_and_load_personality(self):
        personality = Personality(extraversion=9,agreeableness=2,motivated=5, suspicious=1,custom_traits_path=self.temp_file)
        Personality.save_personality(personality,'p1.json')

        personality2 = Personality.load_personality('p1.json')
        assert personality.traits == personality2.traits
        assert personality.custom_traits == personality2.custom_traits
