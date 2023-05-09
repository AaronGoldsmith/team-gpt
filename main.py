import json
# from prompt_generator.PromptGenerator import PromptGenerator
from prompt_generator.personalities.Personality import Personality
if __name__ == '__main__':
    serious_personality = Personality(extraversion=1,agreeableness=2,serious=9)
    fun_personality = Personality(extraversion=9,agreeableness=2,motivated=5, suspicious=1)
    Personality.save_personality(fun_personality,'fun.json')
    Personality.save_personality(serious_personality,'serious.json')
