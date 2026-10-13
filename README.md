# Cybersecurity Projects — Neha Biradar

A collection of educational cybersecurity projects with runnable code and implementation notes. Perform scanning only on localhost, lab systems, or targets you are explicitly authorized to assess.

## Projects

| Task | Project | Contents |
|---|---|---|
| 1 | Network Sniffer | Scapy packet capture and analysis |
| 2 | Phishing Awareness | Awareness guide and quiz |
| 3 | Secure Coding Review | Vulnerable training app, secure remediation, tests |
| 4 | Password Strength Analyzer | Hidden-input CLI, strength heuristics, secure random suggestion |
| 5 | Mini Vulnerability Scanner | TCP port checks and HTTP security-header report |
| 6 | Phishing Email Detection | Scikit-learn TF-IDF + Logistic Regression, metrics and confusion matrix |
| 7 | Secure Login System | Flask + SQLite, password hashing, parameterized queries, sessions and logout |

## Quick start

Each project folder contains its own README and setup instructions. Python 3.10+ is recommended. Install dependencies from the relevant `requirements.txt` file when present.

## Important limitations
- The password analyzer uses simple educational heuristics; it does not check breached-password databases or store password history.
- The mini scanner is a lightweight checker, not a full vulnerability scanner and does not reliably fingerprint outdated software.
- The phishing classifier requires a properly sourced labelled dataset; its metrics must be measured on that dataset and are not guaranteed.
- The login app is a local educational demo and needs additional controls before production use.

## Ethics and privacy
Use only systems you own or have written permission to test. Never commit real passwords, private email datasets, database files, API keys, or production secrets.