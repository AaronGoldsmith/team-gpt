import json
# from prompt_generator.PromptGenerator import PromptGenerator
from prompt_generator.personalities.Personality import Personality
if __name__ == '__main__':
    # professions = prompt_generator.generate_professions(['Doctor', 'Boxer', 'Astronaut'])
    # generator = PromptGenerator()
    # description = generator.get_trait_description('Shy')
    personality1 = Personality(extraversion=9,agreeableness=2,serious=4)
    personality2 = Personality(extraversion=9,agreeableness=2,motivated=5, suspicious=1,custom_traits_path="generated/traits.json")
    Personality.save_personality(personality2,'p1.json')

    personality3 = Personality.load_personality('p1.json')
    print(personality2.traits == personality3.traits)
    print(personality2.custom_traits == personality3.custom_traits)
    print(json.dumps(personality2.__dict__,indent=2))
    print(json.dumps(personality3.__dict__,indent=2))
