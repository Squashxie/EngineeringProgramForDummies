import openai

openai.api_key = 'your open ai key'

def generate_story(prompt):
    response = openai.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=500
    )
    return response.choices[0].text.strip()
def get_user_input():
    genre = input("What kind of story do you want to create? (e.g., adventure, fantasy): ")
    topic = input("What topic are you interested in? (e.g., space exploration, enchanted forests): ")
    return f"Write a {genre} story about {topic}."

story_prompt = get_user_input()
story = generate_story(story_prompt)
print(story)







