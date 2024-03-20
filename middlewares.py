import asyncio
import threading

import aiohttp
from django.utils import timezone


class RequestLoggerMiddleware:
    """
    Use this middleware in your client's django application to log requests onto this server
    """
    def __init__(self, get_response):
        self.get_response = get_response
        self.loop = None
        self.thread = None

    async def async_log(self, params: dict):
        async def send_request():
            data = {
                'response_code': params.get('response_code'),
                'method': params.get('method'),
                'url': params.get('url'),
                'request_received_at': params.get('request_received_at'),
                'response_received_at': params.get('response_received_at'),
            }
            headers = {'Content-Type': 'application/json'}

            async with aiohttp.ClientSession() as session:
                async with session.post(data['url'], json=data, headers=headers) as response:
                    pass

        if not params['url'].startswith('/api/loggers/create_trusted_log/'):
            if self.loop is None:
                self.loop = asyncio.new_event_loop()
                self.thread = threading.Thread(target=self.run_loop)
                self.thread.start()
            asyncio.run_coroutine_threadsafe(send_request(), self.loop)

    def run_loop(self):
        asyncio.set_event_loop(self.loop)
        self.loop.run_forever()

    def __call__(self, request):
        request_time = timezone.now()
        response = self.get_response(request)
        response_time = timezone.now()
        details = {
            'response_code': response.status_code,
            'method': request.method.lower(),
            'url': request.url,
            'request_received_at': request_time.strftime('%Y-%m-%d %H:%M:%S'),
            'response_received_at': response_time.strftime('%Y-%m-%d %H:%M:%S'),
        }

        try:
            asyncio.get_event_loop().run_until_complete(self.async_log(details))
        except RuntimeError:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(self.async_log(details))
        return response
