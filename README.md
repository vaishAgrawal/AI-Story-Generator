# 📖 AI Story Generator

An AI-powered Story Generator built using **Python, FastAPI, Streamlit, LangChain, and Google Gemini**. Users can generate creative stories by selecting a genre, providing characters, and choosing the story length.

---
## Link - https://ai-story-generator-streamlit.onrender.com

## 🚀 Features

- Generate AI-powered stories
- Multiple genres (Horror, Fantasy, Romance, etc.)
- Custom characters
- Short, Medium, and Long story options
- Clean and simple UI
- FastAPI backend
- Google Gemini LLM
- LangChain Prompt Templates

---

## 🛠 Tech Stack

### Frontend
- Streamlit

### Backend
- FastAPI

### AI Framework
- LangChain

### LLM
- Google Gemini 2.5 Flash

### Language
- Python

---

## 📂 Project Structure

```
AI-Story-Generator/
│
├── backend/
│   ├── app.py
│   ├── story.py
│   ├── requirements.txt
│
├── frontend/
│   └── app.py
│
├── .gitignore
├── .env.example
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/vaishAgrawal/AI-Story-Generator.git
```

```bash
cd AI-Story-Generator
```

---

### Create Virtual Environment

```bash
python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

Mac/Linux

```bash
source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r backend/requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file inside the `backend` folder.

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

---

## ▶️ Run Backend

```bash
cd backend
uvicorn app:app --reload
```

Backend will run on:

```
http://127.0.0.1:8000
```

Swagger Docs:

```
http://127.0.0.1:8000/docs
```

---

## ▶️ Run Frontend

Open another terminal.

```bash
cd frontend
streamlit run app.py
```

---

## 📌 How It Works

1. User selects a genre.
2. User enters characters.
3. User selects story length.
4. FastAPI receives the request.
5. LangChain creates a prompt.
6. Gemini generates the story.
7. Story is displayed in Streamlit.

---

## 🔮 Future Improvements

- Story download as PDF
- Story history
- Voice narration
- Multiple language support
- Image generation for stories
- User authentication

---

## 👩‍💻 Author

**Vaishnavi Agrawal**

GitHub:
https://github.com/vaishAgrawal

---

## ⭐ If you like this project

Please consider giving this repository a ⭐ on GitHub.
