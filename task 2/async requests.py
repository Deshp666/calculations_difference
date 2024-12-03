from asyncio import timeout

import httpx
import asyncio
import time


async def fetch_url(client, url):
    response = await client.get(url, timeout=60)
    return response.text


async def fetch_all(urls):
    async with httpx.AsyncClient() as client:
        tasks = [fetch_url(client, url) for url in urls]
        return await asyncio.gather(*tasks)

async def main():
    urls = ["https://jsonplaceholder.typicode.com/posts/55"] * 150
    start_time = time.time()
    results = await fetch_all(urls)
    print(f"Fetched {len(results)} pages.")
    print("Time taken (async with httpx):", time.time() - start_time)

asyncio.run(main())
