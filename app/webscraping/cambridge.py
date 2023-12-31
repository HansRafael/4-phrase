from bs4 import BeautifulSoup

from app.domain.dictionary import Dictionary, MeaningWord, Sources
from app.configs.logger import get_logger

logger = get_logger(__name__)

class CambridgeScraping():
    def __init__(self, web_response, url) -> Dictionary:
        self.web_page = BeautifulSoup(web_response, 'html.parser')
        self.dictionary = Dictionary(source=Sources.CAMBRIDGE_DICTIONARY.value, source_url=url)

    def get_definition_from_cambridge_dictionary(self):
        try:
            senses = self.web_page.find_all('div', class_='def-block ddef_block')
            if not senses:
                return {}
            
            for s in senses:
                meaning = MeaningWord()
                definition = s.find('div', class_='def ddef_d db').text
                meaning.definition = definition

                examples = s.find_all('div', class_='def-body ddef_b')
                for e in examples:
                    for ex in e.find_all('span', class_='eg deg'):
                        if ex:
                            meaning.examples.append(ex.text)
                self.dictionary.meaning.append(meaning)
        except Exception as ex:
            logger.warning(ex)

        return self.dictionary
    