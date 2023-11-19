"""
Urban Dictionary API Response

"list": [
    {
        "definition": str,
        "permalink": str,
        "thumbs_up": int,
        "author": str,
        "word": str,
        "defid": int,
        "current_vote": int,
        "written_on": date,
        "example": str
        "thumbs_down": int
    }
]
"""

from app.domain.dictionary import Dictionary, MeaningWord, Sources
from app.configs.logger import get_logger

logger = get_logger(__name__)

class MapUrbanDictionaryToDictionary:
    def __init__(self, url: str) -> None:
        self.dictionary = Dictionary(source=Sources.URBAN_DICTIONARY.value, source_url=url)
    
    def mapper(self, definition: list):
        definition = definition.get("list")
        if not definition:
            return {}
        
        definition.sort(key = lambda word : (word["thumbs_up"]), reverse=True)
        meanings = []
        try:            
            for word in definition[0:3]:
                meanings.append(MeaningWord(
                    definition=word.get('definition'),
                    examples=[word.get('example')]
                ))
            self.dictionary.meaning = meanings
            self.dictionary.source_url = definition[0].get('permalink')
        except Exception as ex:
            logger.warning(ex)
        
        return self.dictionary