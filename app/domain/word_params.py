from typing import Optional
from pydantic import BaseModel, validator

class WordQueryParams(BaseModel):
    word: str
    expression: Optional[str]

    @validator('word')
    def adding_dash_input(cls, value: str):
        return value.replace(" ", "-")

