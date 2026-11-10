# 🕵️ CaseCraft — AI Mystery Investigation Game

**CaseCraft** is a cinematic mystery investigation game where players explore crime scenes, collect evidence, investigate suspects, connect clues, and solve fictional cases.

The goal is to create an interactive detective experience combining game mechanics, backend development, and AI-powered investigation assistance.

## 🚧 Project Status

**In Development**

## ✨ Planned Features

- Interactive mystery cases and crime-scene exploration
- Evidence collection and investigation
- Suspect profiles and interrogation
- Evidence connections and investigation timelines
- AI-powered hints and explanations
- Case scoring and progress tracking
- Multiple mystery scenarios

## 🛠️ Tech Stack

**Backend**
- Python
- FastAPI
- SQLite
- SQLAlchemy
- Pydantic

**Frontend**
- HTML5
- CSS3
- Vanilla JavaScript

**Testing**
- Pytest

**Planned**
- LLM integration for AI-powered hints
- Advanced evidence analysis and game mechanics

## 📌 Current Progress

- [x] GitHub repository created
- [x] FastAPI backend setup
- [x] SQLite database integration
- [x] Database models for cases, suspects, clues, and investigations
- [x] REST API endpoints for case and investigation management
- [x] API testing with Swagger UI
- [x] Automated backend tests (26 passing)
- [x] Cinematic frontend main menu
- [x] Case briefing screen
- [x] Interactive crime-scene exploration
- [x] Evidence collection and duplicate prevention
- [x] Dynamic clue counter
- [x] Evidence discovery notifications
- [ ] Frontend-backend integration
- [ ] Suspect interrogation gameplay
- [ ] Interactive evidence board
- [ ] AI-powered hints
- [ ] Final accusation and scoring system

## 🎯 Learning Goals

- Build and test REST APIs using FastAPI
- Develop an interactive full-stack application
- Design database models and relationships
- Implement game state and investigation logic
- Integrate LLMs responsibly
- Follow professional Git and GitHub practices

## ▶️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Apurva-Guleria/casecraft.git
cd casecraft
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r backend/requirements.txt
```

### 4. Run the backend

```bash
uvicorn backend.app.main:app --reload
```

### 5. Explore the API

Open:

http://127.0.0.1:8000/docs

## 📂 Project Structure

```text
casecraft/
│
├── backend/
│   └── app/
│       ├── main.py
│       ├── database.py
│       └── models.py
│
├── frontend/
│   ├── index.html
│   ├── assets/
│   ├── css/
│   │   └── style.css
│   └── js/
│       ├── app.js
│       ├── api.js
│       └── game.js
│
├── tests/
├── README.md
└── .gitignore
```

## ⚠️ Disclaimer

All cases, characters, and investigation scenarios are fictional and created for entertainment purposes.

---

**Built with curiosity, Python, and a passion for solving mysteries.** 🔍