from dotenv import load_dotenv
import os

from pet_app import OpenAI

load_dotenv()

print("Agentic AI!")
client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

response_for = client.chat.completions.create(
    model="meta-llama/llama-3.1-8b-instruct",
    messages=[
        {
            "role": "system",
            "content": "You are an aggressive debater who argues FOR artificial intelligence replacing human jobs.",
        },
        {"role": "user", "content": "Should AI replace human jobs? in very short"},
    ],
    stream=True,
)
for chunk in response_for:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="", flush=True)
print()
response_against = client.chat.completions.create(
    model="meta-llama/llama-3.1-8b-instruct",
    messages=[
        {
            "role": "system",
            "content": "You are an aggressive debater who argues AGAINST artificial intelligence replacing human jobs.",
        },
        {"role": "user", "content": "Should AI replace human jobs? in very short"},
    ],
    stream=True,
)

for chunk in response_against:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="", flush=True)
print()
