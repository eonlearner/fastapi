# main.py
# Import FastAPI
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
import api

# Initialize the app
app = FastAPI()

app.include_router(api.router)

origins = [
    "http://localhost:3000",
    "localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# GET operation at route '/'
@app.get('/')
def root_api():
    return {"message": "Welcome to EonLearning Lms App"}
