from fastapi import FastAPI
from pydantic import BaseModel
from story import generate_story

app = FastAPI()


class StoryRequest(BaseModel):
    genre: str
    characters: str
    length: str


@app.get("/")
def home():
    return {"message": "Story Generator Running"}


@app.post("/story")
def story(request: StoryRequest):

    result = generate_story(
        request.genre,
        request.characters,
        request.length
    )

    return {"story": result}