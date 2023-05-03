import json
from prompt_generator.PromptGenerator import PromptGenerator

class TestPromptGenerator():

    def setup_method(self):
        self.prompt_generator = PromptGenerator()

    def test_generate_professions(self):
        professions = ['Doctor', 'Sushi Chef', 'Chocolatier', 'Construction Worker', 'Engineer', 'Product Manager']
        number_allowed = 2
        generated_professions = self.prompt_generator.generate_professions(number_allowed, professions)
        # check that each expected key is present in the response dict
        # check that we have the expected number of keys in our list
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

    def test_generate_random_professions(self):
        number_allowed = 3
        generated_professions = self.prompt_generator.generate_professions(number_allowed)
        # Check that the generated professions are random by comparing with multiple runs
        generated_professions_2 = self.prompt_generator.generate_professions(number_allowed)
        assert generated_professions != generated_professions_2

    def test_generate_single_profession(self):
        number_allowed = 1
        profession = 'Doctor'
        generated_professions = self.prompt_generator.generate_professions(number_allowed, [profession])
        parsed_professions = json.loads(generated_professions)
        assert len(parsed_professions['professions']) == number_allowed
        assert parsed_professions['professions'][0]['name'] == profession

    def test_generate_invalid_num_professions(self):
        number_allowed = -1
        professions = ['Doctor', 'Sushi Chef']
        try:
            generated_professions = self.prompt_generator.generate_professions(number_allowed, professions)
            assert False, "Expected an error when using an invalid value for num_professions"
        except ValueError:
            pass

    def test_generate_invalid_professions_type(self):
        number_allowed = 2
        professions = "Doctor"  # Should be a list, not a single string
        try:
            generated_professions = self.prompt_generator.generate_professions(number_allowed, professions)
            assert False, "Expected an error when using an invalid type for professions"
        except TypeError:
            pass

