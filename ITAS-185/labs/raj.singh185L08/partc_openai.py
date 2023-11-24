"""
Course: ITAS 185 - Introduction to Programming
Lab08: OpenAI Children's Story Author
Description:
    This script defines a StoryAuthor class capable of generating stories. It takes user input
    for an animal, a body part, and a landscape/timeframe setting. Utilizing the OpenAI GPT model,
    it generates a children's story based on the provided inputs.
"""

import openai

class StoryAuthor:
    """Generate stories based on user inputs using the openai GPT model."""

    def __init__(self):
        """Initializes the StoryAuthor class without any attributes."""
        self.animal = None
        self.body_part = None
        self.landscape_timeframe = None

    def get_inputs(self):
        """Prompts the user to input an animal, a body part, and a landscape/timeframe."""
        self.animal = input("Enter an animal: ")
        self.body_part = input("Enter a body part: ")
        self.landscape_timeframe = input("Enter a landscape/timeframe: ")

    def generate_story(self):
        """Generates a story using the OpenAI GPT model based on user inputs.

        Returns:
            A string containing the generated story.
        """
        completion = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[
                {
                    "role": "system",
                    "content": f"You are a wise author who pens children's stories, intended for first grade level, with a minimum of 300 words, set in the timeframe of {self.landscape_timeframe}."
                },
                {
                    "role": "user",
                    "content": f"In {self.landscape_timeframe}, there lived a smart {self.animal} with a *insert a debilitation* {self.body_part}."
                }
            ]
        )
        return completion.choices[0].message['content']


# Create an instance of the story generator
story_bot = StoryAuthor()

# Prompt input from the user
story_bot.get_inputs()

# Generate the story and print it
story = story_bot.generate_story()
print(story)
