from fastapi import APIRouter, Request, status
from typing import List
from app.openai.request import create_request


router = APIRouter(prefix="/phrase",
    tags=["Phrase"])

@router.get("/")
def get_phrase(request: Request):
    create_request()
    return "Hello world"