Deep analysis and execution notes:

- db_service uses 'db is not None' to avoid PyMongo truth-testing error.
- The backend will use in-memory fallback if pymongo is not installed or Mongo unreachable.
- Auth uses werkzeug hashing and a simple dev token; swap to Flask-JWT-Extended for production.
- Vite dev server proxies /api to backend to avoid CORS.
- Seed script (backend/seed.py) will populate Mongo when pymongo is installed; otherwise run manually.
- For production, build frontend and serve static files from backend/app/static.
