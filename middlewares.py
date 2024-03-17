import asyncio
import threading

import aiohttp
from django.conf import settings


class RequestLoggerMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    address = settings.LOGGING_API

    async def __call__(self, request):
        print(request.path)
        print(request.get_full_path())

        async def send_request():
            # url = self.address
            url = 'http://127.0.0.1:5555/api/loggers/create_trusted_log/'
            data = {
                'response_code': 123,
                'method': "post",
                'url': "github.com2",
                'request_received_at': "2024-03-17T12:04:01+05:30",
                'response_received_at': "2024-03-17T12:04:03+05:30",
            }
            headers = {'Content-Type': 'application/json'}

            async with aiohttp.ClientSession() as session:
                async with session.post(url, json=data, headers=headers) as response:
                    pass

            new_loop.stop()
            thread.join()

        new_loop = asyncio.new_event_loop()
        thread = threading.Thread(target=new_loop.run_forever)
        thread.start()

        asyncio.run_coroutine_threadsafe(send_request(), new_loop)

        response = await self.get_response(request)
        return response
