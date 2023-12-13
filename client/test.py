import aiohttp
import asyncio
import time

URL = "http://localhost:8000/"
num_requests = 10

PROMPT = "Write quick sort with python"


async def fetch(session, url, prompt):
    async with session.post(url, json={"prompt": prompt}) as response:
        return await response.json()


async def main():
    start_time = time.time()

    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, URL, PROMPT) for _ in range(num_requests)]
        responses = await asyncio.gather(*tasks)

    total_time = time.time() - start_time
    rps = num_requests / total_time
    print(f"Total Time: {total_time:.3f} seconds")
    print(f"RPS: {rps:.3f}")

    with open("responses.txt", "w") as resp_file:
        for idx, response in enumerate(responses):
            code = response['code']
            resp_file.write(f"Result {idx+1}:\n{code}")
            resp_file.write("\n----------------------------\n\n")


asyncio.run(main())
