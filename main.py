from prompt_generator.PromptGenerator import PromptGenerator
from prompt_generator.personalities.Personality import Personality
if __name__ == '__main__':
    # professions = prompt_generator.generate_professions(['Doctor', 'Boxer', 'Astronaut'])
    # generator = PromptGenerator()
    # description = generator.get_trait_description('Partier')
    # personality = Personality(extraversion=1,agreeableness=9,boring=4)
    # personality2 = Personality(extraversion=9,agreeableness=2,selfish=4)
    personality3 = Personality(extraversion=9,agreeableness=2,funny=4)
    personality2 = Personality(extraversion=9,agreeableness=2,funny=4,custom_traits_path="generated/custom_traits.json")


