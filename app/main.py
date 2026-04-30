from fastapi import FastAPI
from dotenv import load_dotenv
import os
from pinecone import Pinecone
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware
# from .routes import fetchVideoDetails_route
from .routes import fetchPdfDetails_route
from .routes import generateQuizes_route
from .routes import tutorExplain_route



# initialize the pinecone client



load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")


if not PINECONE_API_KEY:
    raise ValueError("PINECONE_API_KEY is not set in the environment variables.")


pineconeDB = Pinecone(
    api_key=PINECONE_API_KEY,
)









app = FastAPI()




app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

# app.include_router(fetchVideoDetails_route.router)
app.include_router(fetchPdfDetails_route.router)
app.include_router(generateQuizes_route.router)
app.include_router(tutorExplain_route.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}