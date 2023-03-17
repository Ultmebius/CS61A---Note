import os
import openai
openai.api_key = ('')

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Are you GPT-3.5?"},
    ]
)

print(completion.choices[0].message)
