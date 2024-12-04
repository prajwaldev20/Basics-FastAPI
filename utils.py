# utils.py
import openai

# Set your OpenAI API key
openai.api_key = ""


def generate_description(input):
    messages = [
        {
            "role": "system",
            "content": "As a Product Description Generator, generate multi-paragraph rich text product descriptions with emojis from the information provided to you.",
        },
        {"role": "user", "content": input},
    ]

    try:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
        )
        reply = completion.choices[0].message.content
        return reply
    except Exception as e:
        return f"Error generating description: {str(e)}"
