
from aiohttp import ClientConnectorError, ClientResponse, ClientSession
from fastapi import HTTPException
import requests

from app.configs.logger import get_logger

logger = get_logger(__name__)

class HTTPClient:
    def __init__(self) -> None:
        self.__token = None     
        
    
    async def async_get(self, url: str, session: ClientSession, headers: dict, get_html_page=False, params: dict = {}):
        try:
            async with session.get(url=url, params=params, headers=headers) as response:
                return await self._request_handler(http_response=response, get_html_page=get_html_page)
        except HTTPException as e:
            if e.status_code == 404:
                logger.warning(f'Word not found! :: {url}')
            logger.warning(e.detail)
            return {}
        except ClientConnectorError as ex:
            logger.error(ex.os_error.strerror)
            logger.error(ex.host)
            return {}
        except Exception as ex:
            logger.error(ex)
            return {}

    async def _request_handler(self, http_response: ClientResponse, get_html_page=False):
        if http_response.status == 200:
            try:
                if get_html_page:
                    return await http_response.text()
                return await http_response.json()
            except Exception as ex:
                raise ex
        else:
            try:
                result = await http_response.json(content_type=None)
            except Exception:
                result = http_response.reason
            raise HTTPException(
                status_code=http_response.status,
                detail=str(result))