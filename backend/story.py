import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=1
)

prompt = PromptTemplate.from_template("""
You are a creative story writer.

Write a {length} {genre} story.

Characters:
{characters}

The story should have a beginning, middle and end.
Keep the story engaging.
""")

chain = prompt | llm


def generate_story(genre, characters, length):

    response = chain.invoke(
        {
            "genre": genre,
            "characters": characters,
            "length": length
        }
    )

    return response.content