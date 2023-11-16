from typing_extensions import Annotated
from fastapi import (APIRouter, Depends, Request, status)
from typing import List

from fastapi.responses import JSONResponse
from app.controller.controller_word import ControllerWord
from app.domain.dictionary import DictionaryResponse
from app.http.core_service import CoreService
from app.http.http_client import HTTPClient
from app.domain.word_params import WordQueryParams


router = APIRouter(prefix="/word")

@router.get("/", response_model=DictionaryResponse, tags=["Word"])
def get_phrase(query_params: Annotated[WordQueryParams, Depends()]):
    controller_word = ControllerWord(query_params=query_params)
    response = controller_word.request()
    
    return JSONResponse(status_code=200,content=response.dict())