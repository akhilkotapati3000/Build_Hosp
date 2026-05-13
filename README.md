BuildHosp - Full-stack project (Flask + MongoDB + React + Vite + Tailwind)

Folders:
- backend/ : Flask app and services
- frontend/: Vite + React app

Quick start (local, no Docker):
1. Start backend:
   cd backend
   python -m venv venv
   venv\Scripts\activate   # Windows
   source venv/bin/activate  # macOS/Linux
   pip install -r requirements.txt
   python -m app.main

2. Start frontend:
   cd frontend
   npm install
   npm run dev
