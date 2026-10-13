#!/usr/bin/env python3
"""Local password-strength checker. Passwords are never stored or transmitted."""
import getpass
import re
import secrets
import string

COMMON = {"password", "password123", "123456789", "qwerty123", "letmein", "admin123"}

def analyze(password: str) -> tuple[int, list[str]]:
    score = 0
    tips = []
    if len(password) >= 12: score += 2
    elif len(password) >= 8: score += 1
    else: tips.append("Use at least 12 characters.")
    checks = [
        (r"[a-z]", "Add lowercase letters."),
        (r"[A-Z]", "Add uppercase letters."),
        (r"\d", "Add numbers."),
        (r"[^A-Za-z0-9]", "Add symbols.")
    ]
    for pattern, tip in checks:
        if re.search(pattern, password): score += 1
        else: tips.append(tip)
    if password.lower() in COMMON or re.search(r"(.)\1{3,}", password):
        score = max(0, score - 2)
        tips.append("Avoid common passwords and repeated characters.")
    if re.search(r"password|qwerty|letmein|admin", password, re.I):
        score = max(0, score - 1)
        tips.append("Avoid predictable words and keyboard patterns.")
    return score, tips

def suggestion(length=16):
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*()-_=+"
    while True:
        candidate = "".join(secrets.choice(alphabet) for _ in range(length))
        if (any(c.islower() for c in candidate) and any(c.isupper() for c in candidate)
            and any(c.isdigit() for c in candidate) and any(not c.isalnum() for c in candidate)):
            return candidate

if __name__ == "__main__":
    pw = getpass.getpass("Enter a password (input hidden; not saved): ")
    score, tips = analyze(pw)
    label = "Weak" if score <= 2 else "Moderate" if score <= 4 else "Strong"
    print(f"Assessment: {label} ({score}/6)")
    for tip in tips: print("- " + tip)
    print("Generated alternative (save it in a password manager):", suggestion())
