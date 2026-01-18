"""A Simple API Service"""

from fastapi import FastAPI
import logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

app = FastAPI()

@app.get("/")
def getGreeting():
    logging.info("GET /")
    return {
        "message": "Hello World!"
    }
    
@app.get("/health")
def getStatus():
    logging.info("GET /health")
    return {
        "status": "OK"
    }