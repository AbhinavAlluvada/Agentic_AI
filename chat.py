from dotenv import load_dotenv
import os
from pet_app import OpenAI
load_dotenv()

print("Ask it!")
question = input("Enter a question...")
client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

bot = client.chat.completions.create(
    model="meta-llama/llama-3.1-8b-instruct",
    messages=[
        {"role":"system",
         "content":"You are to the point talker , who doesnt like nonsense but like to add extra useful facts without making the answer long..."},
        {
            "role":"user",
            "content":question
        }
    ],
    stream=True
)

for chunk in bot:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content,end = "",flush=True)
print()