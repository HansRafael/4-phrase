from fastapi import FastAPI
import uvicorn
from routes.api import router
from dotenv import dotenv_values

config = dotenv_values(".env")
app = FastAPI()

app.include_router(router)

if __name__ == '__main__': #this indicates that this a script to be run
    uvicorn.run("main:app", host='127.0.0.1', port=8000, log_level="info", reload = True)