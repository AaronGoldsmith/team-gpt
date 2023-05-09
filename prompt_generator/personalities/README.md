# Team GPT Personalities


### Create a Personality
```python
Personality(extraversion=9,agreeableness=2,serious=4)
```
New traits are saved to the `custom_traits.json` file which can be referenced by all Personalities. 

To specify a custom traits dictionary, provide an additional parameter `custom_traits_path` when initializing the Personality.

```python
# Specify location of the custom personality traits.
Personality(extraversion=9,agreeableness=2,suspicious=1,custom_traits_path="generated/traits.json")
```

### Save a Personality

```python
# Path to save a full Personality
personality_path = "personality_example.json"
custom_personality = Personality(extraversion=9,agreeableness=2,motivated=5, suspicious=1)

# Save the personality 
Personality.save_personality(custom_personality, personality_path)

# Load the saved personality
loaded_personality = Personality.load_personality(personality_path)

# Compare the traits of our custom_personality with the traits of our loaded_personality
print(custom_personality.traits == loaded_personality.traits)
print(custom_personality.custom_traits == loaded_personality.custom_traits)

# Display custom and loaded personalities
print(json.dumps(custom_personality.__dict__,indent=2))
print(json.dumps(loaded_personality.__dict__,indent=2))
```
