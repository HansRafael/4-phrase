
from aiohttp import ClientSession
import requests

class HTTPClient:
    def __init__(self) -> None:
        self.__token = None     
        
    
    async def async_get(self, url: str, session: ClientSession, headers: dict, params: dict = {}):
        try:
            async with session.get(url=url, params=params, headers=headers) as response:
                response = await response.json()
                return response
        except Exception as e:
            return e

    async def async_get_web_response(self, url: str, session: ClientSession, headers: dict, params: dict = {}):
        try:
            async with session.get(url=url, params=params, headers=headers) as response:
                return await response.text()
        except Exception as e:
            return e
    
