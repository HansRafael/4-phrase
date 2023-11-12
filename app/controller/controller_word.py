

import asyncio
from app.domain.dictionary import Dictionary, DictionaryResponse
from app.domain.mapper.map_urban_dictionary import MapUrbanDictionaryToDictionary
from app.domain.word_params import WordQueryParams
from app.http.core_service import CoreService
from app.http.http_client import HTTPClient
from app.webscraping.oxford import OxfordScraping


class ControllerWord:
    def __init__(self, query_params: WordQueryParams, body: dict = None) -> None:
        self.client = HTTPClient()
        self.query_params = query_params
        self.word = query_params.word
        self.core_service = CoreService(client=self.client)

    async def __get_word_definition_from_api(self):
        urban = await self.core_service.get_definition_from_urban_dictionary(word=self.word)
        return urban

    async def __get_word_definition_from_web_scraping(self) -> Dictionary:
        tasks = {
            'oxford_page': self.core_service.get_definition_from_oxford(word=self.word)
        }

        results = await asyncio.gather(*tasks.values())
        results = {key: result for key, result in zip(tasks.keys(), results)}

        return results.get('oxford_page')

    async def __get_word_definition(self) -> Dictionary:
        words = []
        words.append(await self.__get_word_definition_from_api())
        words.append(await self.__get_word_definition_from_web_scraping())

        return words
    
    def request(self) -> DictionaryResponse:
        response = asyncio.run(self.__get_word_definition())

        word = DictionaryResponse(
            word=self.word,
            content=response,
            source_found=len(response),
            definition_found=0)
        word.definition_found = word.count_defnition_founded()
        return word