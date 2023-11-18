from fastapi import APIRouter, HTTPException, Depends
from app.endpoints import phrase, word

router = APIRouter()

#router.include_router(phrase.router)
router.include_router(word.router)