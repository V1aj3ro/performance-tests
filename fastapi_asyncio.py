import asyncio
import datetime
import time

import httpx


async def fetch_url(url: str) -> tuple[int, str]:
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.status_code, response.text[:50]

async def main():
    urls = [
        "https://postman-echo.com/delay/1",
        "https://postman-echo.com/delay/2",
        "https://postman-echo.com/delay/3"

    ]

    results = []

    results = await asyncio.gather(*(fetch_url(url) for url in urls))

    for status, text in results:
        print(f"Response status: {status}, text beginning: {text}")


if __name__ == "__main__":
    start_time = time.perf_counter()
    asyncio.run(main())
    end_time = time.perf_counter()
    print(end_time - start_time)