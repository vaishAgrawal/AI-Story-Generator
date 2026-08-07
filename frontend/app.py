import streamlit as st
import requests
from dotenv import load_dotenv
import os

load_dotenv()

BACKEND_URL = os.getenv("BACKEND_URL")
st.set_page_config(page_title="AI Story Generator")

st.title("📖 AI Story Generator")

genre = st.selectbox(
    "Select Genre",
    [
        "Adventure",
        "Horror",
        "Fantasy",
        "Comedy",
        "Romance",
        "Sci-Fi",
        "Mystery"
    ]
)

characters = st.text_input(
    "Characters",
    placeholder="Example: Dragon, Princess, Wizard"
)

length = st.selectbox(
    "Story Length",
    [
        "Short",
        "Medium",
        "Long"
    ]
)

if st.button("Generate Story"):

    response = requests.post(
        f"{BACKEND_URL}/generate-story",
        json={
            "genre": genre,
            "characters": characters,
            "length": length
        }
    )

    story = response.json()["story"]

    st.subheader("Generated Story")

    st.write(story)