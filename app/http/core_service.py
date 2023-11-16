

import aiohttp
from app.configs.environment import Environment
from app.domain.dictionary import Dictionary
from app.domain.mapper.map_urban_dictionary import MapUrbanDictionaryToDictionary
from app.http.http_client import HTTPClient
from app.webscraping.cambridge import CambridgeScraping
from app.webscraping.oxford import OxfordScraping


class CoreService:
    def __init__(self, client: HTTPClient) -> None:
        self.client = client
        self.env = Environment()
    

    async def get_definition_from_urban_dictionary(self, word: str):
        url = self.env.URBAN_DICTIONARY_URI
        headers = {
	        "X-RapidAPI-Key": Environment.X_RAPID_API_KEY,
	        "X-RapidAPI-Host": "mashape-community-urban-dictionary.p.rapidapi.com"
        }
        params = {"term": word}

        async with aiohttp.ClientSession() as sessesion:
            response = await self.client.async_get(url=url, session=sessesion,headers=headers, params=params)

        if response:
            response = MapUrbanDictionaryToDictionary(url=url+word).mapper(response)
            return response
        return {}
    
    async def get_definition_from_oxford(self, word: str) -> Dictionary:
        url = self.env.OXFORD_DICTIONARY_URI + word
        headers = { "User-Agent": "" }

        async with aiohttp.ClientSession() as sessesion:
            web_page = await self.client.async_get(url=url, session=sessesion,headers=headers,get_html_page=True)
    
        if web_page:
            web_page = OxfordScraping(web_response=web_page, url=url)
            return web_page.get_definition_from_oxford_dictionary()
        return {}

    async def get_definition_from_cambridge(self, word: str) -> Dictionary:
        url = self.env.CAMBRIDGE_DICTIONARY_URI + word
        headers = { "User-Agent": "" }

        async with aiohttp.ClientSession() as sessesion:
            web_page = await self.client.async_get(url=url, session=sessesion,headers=headers,get_html_page=True)
    
        if web_page:
            web_page = CambridgeScraping(web_response=web_page, url=url)
            return web_page.get_definition_from_cambridge_dictionary()
        return {}




