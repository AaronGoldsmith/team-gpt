import json
from ..prompt_generator.PromptGenerator import PromptGenerator

class TestPromptGenerator():

    def setup_method(self):
        self.prompt_generator = PromptGenerator()

    def test_generate_professions(self):
        professions = ['Doctor', 'Sushi Chef', 'Chocolatier', 'Construction Worker', 'Model', 'Product Manager']
        number_allowed = 5
        generated_professions = self.prompt_generator.generate_professions(number_allowed, professions)
        # test that each expected key is present in the response dict
        try:
            parsed_professions = json.loads(generated_professions)
            assert isinstance(parsed_professions, dict)
            assert 'professions' in parsed_professions
            assert isinstance(parsed_professions['professions'], list)
            assert len(parsed_professions['professions']) == number_allowed
            for profession in parsed_professions['professions']:
                assert isinstance(profession, dict)
                assert 'name' in profession
                assert 'known_for' in profession
                assert 'lesser_known_for' in profession
                assert 'contribution' in profession
        except json.JSONDecodeError:
            assert False, 'Generated professions cannot be parsed as JSON'
