from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from .routes import fetchVideoDetails_route
from .routes import fetchPdfDetails_route
from .routes import generateQuizes_route
from .routes import tutorExplain_route


app = FastAPI()
app.include_router(fetchVideoDetails_route.router)
app.include_router(fetchPdfDetails_route.router)
app.include_router(generateQuizes_route.router)
app.include_router(tutorExplain_route.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}