import os
import openai
openai.api_key = (' ')

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "tell me how to realize fib in python"},
    ]
)

print(completion.choices[0].message)
