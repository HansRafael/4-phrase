from bs4 import BeautifulSoup

from app.domain.dictionary import Dictionary, MeaningWord, Sources


class OxfordScraping():
    def __init__(self, web_response, url) -> Dictionary:
        self.web_page = BeautifulSoup(web_response, 'html.parser')
        self.dictionary = Dictionary(source=Sources.OXFORD_DICTIONARY.value, source_url=url)

    def get_definition_from_oxford_dictionary(self):
        senses = self.web_page.find_all('li', class_='sense')
        
        for s in senses:
            meaning = MeaningWord()
            definition = s.find('span', class_='def').text
            meaning.definition = definition

            examples = s.find_all('ul', class_='examples')
            for e in examples:
                for ex in e.find_all('li'):
                    meaning.examples.append(ex.text)
            self.dictionary.meaning.append(meaning)
        
        return self.dictionary
    