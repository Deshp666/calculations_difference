import asyncio
import time


async def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

async def compute_factorials(numbers):
    tasks = [factorial(num) for num in numbers]
    results = await asyncio.gather(*tasks)
    return results

async def main():
    numbers = [150000, 150001, 150002]
    start_time = time.time()
    await compute_factorials(numbers)
    print("Time taken:", time.time() - start_time)

asyncio.run(main())
