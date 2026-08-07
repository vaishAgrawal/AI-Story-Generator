import streamlit as st
import requests

BACKEND_URL = "https://ai-story-generator-56j9.onrender.com"

st.set_page_config(page_title="AI Story Generator")

st.title("📖 AI Story Generator")

genre = st.selectbox(
    "Select Genre",
    ["Adventure", "Horror", "Fantasy", "Comedy", "Romance", "Sci-Fi", "Mystery"]
)

characters = st.text_input(
    "Characters",
    placeholder="Example: Dragon, Princess, Wizard"
)

length = st.selectbox(
    "Story Length",
    ["Short", "Medium", "Long"]
)

if st.button("Generate Story"):

    response = requests.post(
        "https://ai-story-generator-56j9.onrender.com/story",
        json={
            "genre": genre,
            "characters": characters,
            "length": length
        },
        timeout=60
    )

    if response.status_code == 200:
        st.subheader("Generated Story")
        st.write(response.json()["story"])
    else:
        st.error(response.text)