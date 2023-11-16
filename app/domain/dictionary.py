
from enum import Enum
from typing import List, Optional
from pydantic import BaseModel

class Sources(str, Enum):
    URBAN_DICTIONARY = 'Urban Dictionary'
    OXFORD_DICTIONARY = 'Oxford Dictionary'
    CAMBRIDGE_DICTIONARY = 'Cambridge Dictionary'

class MeaningWord(BaseModel):
    definition: str = ''
    examples: List[str] = []

class Dictionary(BaseModel):
    source: Sources
    source_url: Optional[str]
    source_logo: Optional[str]
    meaning: List[MeaningWord] = []
    definition_image: Optional[str]

    class Config:  
        use_enum_values = True

class DictionaryResponse(BaseModel):
    word: str
    content: List[Dictionary]
    source_found: int
    definition_found: int

    def count_definition_founded(self) -> int:
        definition_found = 0
        if self.content:
            for source in self.content:
                definition_found += len(source.meaning)
        return definition_found



    