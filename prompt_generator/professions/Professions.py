from typing import List, Optional

def generate_professions(num_professions: int, professions: Optional[List[str]] = None) -> List[str]:
    """
    Generates a list of professions based on the input parameters.

    Args:
        num_professions (int): The number of professions to return.
        professions (list, optional): An optional list of professions to select from.

    Returns:
        string: A JSON string of professions based on the input parameters with keys `name`, `known_for`, `lesser_known_for`, `contribution`
    """

    instruct = ""

    if num_professions is None or not isinstance(num_professions, int):
        raise ValueError("num_professions must be provided as an argument")
    if num_professions < 1:
        raise ValueError(f"num_professions must be greater than 0, you provided {num_professions}")
    
    # Setup instructions for user provided input
    if professions is None:
        professions = []
    elif len(professions)>num_professions:
        professions = professions[:num_professions]
        instruct = f"\nInclude professions exclusively from the list: {str(professions)}"
    else:
        num_diff = num_professions - len(professions)
        instruct = f"\nInclude all professions from the list: {str(professions)} and { num_diff } other professions"
    
     # Check if we have more items in the professions list than we can provide a response for
    # if(len(professions)>num_professions):
    #     professions = professions[:num_professions]
    
    # num_diff = abs(num_professions - len(professions))

    
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
    {instruct}
    """
    return prompt