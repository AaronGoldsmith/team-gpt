
def generate_professions(num_professions: int, professions=None):
    # Default value
    if professions is None:
        professions = ["None provided"]
    
     # Check if we have more items in the professions list than we can provide a response for
    if(len(professions)>num_professions):
        professions = professions[:num_professions]
    
    num_diff = abs(num_professions - len(professions))

    prompt = f"""
    Please provide a JSON-formatted string containing a list of {num_professions} distinct professions in any field along with their skills/expertise. For each profession, include what they are known for, what they might not be very well known for, and how they could contribute to a cross-functional team project. 
    The JSON string should look like the following example:
    {{
      "professions": [
        {{
          "name": "<Profession 1>",
          "known_for": "<What the profession is known for>",
          "lesser_known_for": "<What the profession might not be very well known for>",
          "contribution": "<How the profession could contribute to a team project>"
        }},
        {{
          "name": "<Profession 2>",
          "known_for": "<What the profession is known for>",
          "lesser_known_for": "<What the profession might not be very well known for>",
          "contribution": "<How the profession could contribute to a team project>"
        }},
        // ...and so on for the other professions
      ]
    }}
    Include professions from the list: {str(professions)} and { num_diff } other professions
    """
    return prompt