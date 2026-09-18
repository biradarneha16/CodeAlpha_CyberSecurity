# Task 3 — Secure Coding Review

A deliberately vulnerable Flask application is provided as a local training target.

Files: `vulnerable_app.py` (insecure target), `secure_app.py` (remediated reference), `SECURE_CODING_REVIEW.md` (findings), and `test_security.py` (tests).

Setup:
```bash
python -m pip install -r requirements.txt
python vulnerable_app.py
```
The target binds only to 127.0.0.1. Review areas: SQL injection, XSS, password handling, CSRF, debug configuration, security headers, and input validation.
