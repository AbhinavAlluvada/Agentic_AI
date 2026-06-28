import asyncio
import httpx
url = "https://jsonplaceholder.typicode.com/users"
async def main():
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        users = response.json()
        print(users[0]["name"])
asyncio.run(main())