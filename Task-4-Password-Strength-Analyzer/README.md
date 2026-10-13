# Task 4 — Password Strength Analyzer

A local Python CLI tool that checks length, character variety, and common/predictable patterns. It uses `getpass` so typed input is hidden, `secrets` for secure random generation, and never saves or transmits passwords.

## Run
```bash
python3 password_analyzer.py
```

## Security notes
- This is an educational heuristic, not a password-cracking estimator or breach database check.
- Unique passwords and a reputable password manager are recommended; prefer long passphrases.
- Never enter a real password into a website or tool you do not trust.
- No password history database is implemented, so reuse detection is not claimed.
