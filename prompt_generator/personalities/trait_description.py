def generate_trait_description(trait):
    prompt = f"Generate a simple 1 sentence description of the following personality\
              trait and return it as JSON. For example\
              curiosity --> {{\"curiosity\": \"A measure of one's interest in learning new things.\"}}\
              Personality Trait: {trait} ---> \
              "
    return prompt
