# Task 7 — Secure Login System

## Run locally
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export FLASK_SECRET_KEY="$(python -c 'import secrets; print(secrets.token_hex(32))')"
python app.py
```
Open http://127.0.0.1:5000. The app uses Werkzeug's scrypt password hashing, parameterized SQLite queries, basic validation, generic login errors, session clearing, logout, and response security headers.

## Important production gaps
This is an educational local demo, not production-ready. Before deployment add CSRF protection, rate limiting / lockout controls, HTTPS, secure cookie settings, password reset protections, MFA, audit logging, and managed secret storage. Never expose Flask's development server publicly or commit real secrets or user databases.
