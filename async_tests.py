import asyncio
import timeit

import aiohttp


async def send_post_request(session, url, headers, data):
    async with session.post(url, headers=headers, json=data) as response:
        pass
        # response_text = await response.text()
        # if response.status not in (201, 202):  # Check if status code is not 201 or 202
        #     print("Error")
        # else:
        #     print(f"Response: {response_text}")


async def main():
    url = "http://127.0.0.1:5555/backend/api/loggers/create_trusted_log/"
    headers = {"Content-Type": "application/json"}
    data = {
        "response_code": 2341,
        "method": "post",
        "url": "githudfdfdfb.com2",
        "request_received_at": "2024-03-17T12:04:01+05:30",
        "response_received_at": "2024-03-17T12:04:03+05:30"
    }

    num_requests = 50000
    async with aiohttp.ClientSession() as session:
        tasks = []
        for _ in range(num_requests):
            tasks.append(send_post_request(session, url, headers, data))

        print('Async Requests dispatched successfully ')
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    execution_time = timeit.timeit(lambda: asyncio.run(main()), number=1)
    print("Execution time", execution_time)
