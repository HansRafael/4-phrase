

import asyncio
from app.domain.dictionary import Dictionary, DictionaryResponse
from app.domain.mapper.map_urban_dictionary import MapUrbanDictionaryToDictionary
from app.domain.word_params import WordQueryParams
from app.http.core_service import CoreService
from app.http.http_client import HTTPClient

from app.configs.logger import get_logger

logger = get_logger(__name__)

class ControllerWord:
    def __init__(self, query_params: WordQueryParams, body: dict = None) -> None:
        self.client = HTTPClient()
        self.query_params = query_params
        self.word = query_params.word
        self.core_service = CoreService(client=self.client)

    async def __get_word_definition_from_api(self) -> [Dictionary]:
        urban = await self.core_service.get_definition_from_urban_dictionary(word=self.word)
        return [urban]

    async def __get_word_definition_from_web_scraping(self) -> [Dictionary]:
        tasks = {
            'oxford': self.core_service.get_definition_from_oxford(word=self.word),
            'cambridge': self.core_service.get_definition_from_cambridge(word=self.word),
            'britannica': self.core_service.get_definition_from_britannica(word=self.word)
        }

        return await asyncio.gather(*tasks.values())

    async def __get_word_definition(self) -> Dictionary:
        logger.info(f'Starting process to get definition for {self.word.upper()} word.')

        words = [
            *await self.__get_word_definition_from_web_scraping(),
            *await self.__get_word_definition_from_api()
        ]

        words = [word for word in words if word != {}]
        logger.info('Ending process.')
        return words
    
    def request(self) -> DictionaryResponse:
        response = asyncio.run(self.__get_word_definition())

        word = DictionaryResponse(
            word=self.word,
            content=response,
            source_found=len(response),
            definition_found=0)
        word.definition_found = word.count_definition_founded()
        return word