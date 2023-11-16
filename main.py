from fastapi import FastAPI
import uvicorn
from app.configs.environment import Environment
from routes.api import router

config = Environment()
app = FastAPI(title="4-Phrase API", version="0.1", openapi_url="/openapi.json")

app.include_router(router)

if __name__ == '__main__': #this indicates that this a script to be run
    uvicorn.run("main:app", host=config.HOST, port=int(config.PORT), log_level="info", reload = True)