import asyncio
from client import AIClient
from dotenv import load_dotenv
import os
import json

load_dotenv()


async def main():
    client = AIClient(
        os.getenv("API_KEY_NEW"),
        model="gemini-2.5-flash",
        base_url="https://generativelanguage.googleapis.com",
    )

    while True:
        prompt = input("Enter a prompt: ")
        answer = await client.send_prompt(prompt)
        if prompt == "exit":
            return "Thank You"
        else:
            print(answer)

            data = {"You": prompt, "AI": answer}
            with open("chat_history.jsonl", "a") as file:
                json.dump(data, file)
                file.write("\n")


asyncio.run(main())
