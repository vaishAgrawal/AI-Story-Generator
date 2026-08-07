import streamlit as st
import requests


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
        "https://ai-story-generator-56j9.onrender.com",
        json={
            "genre": genre,
            "characters": characters,
            "length": length
        }
    )

    if response.status_code == 200:
        story = response.json()["story"]

        st.subheader("Generated Story")
        st.write(story)

    else:
        st.error(f"Backend Error: {response.text}")