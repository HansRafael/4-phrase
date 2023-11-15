from fastapi import FastAPI
import uvicorn
from app.configs.environment import Environment
from routes.api import router
from dotenv import dotenv_values

config = Environment()
app = FastAPI()

app.include_router(router)

if __name__ == '__main__': #this indicates that this a script to be run
    uvicorn.run("main:app", host=config.HOST, port=int(config.PORT), log_level="info", reload = True)