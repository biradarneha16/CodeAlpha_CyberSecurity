# Task 3 Report — Secure Coding Review

## Findings

| ID | Vulnerability | Evidence | Remediation |
|---|---|---|---|
| SC-01 | SQL injection | `/search` concatenates q into SQL | Parameterized query |
| SC-02 | XSS | `/hello` inserts name into HTML | Output encoding |
| SC-03 | Weak password handling | Plaintext comparison model | Password hashing and verification |
| SC-04 | Missing CSRF | State-changing endpoint has no token check | CSRF token validation |
| SC-05 | Debug exposure | `debug=True` | Disable debug outside development |
| SC-06 | Missing security headers | No response headers | CSP, nosniff, Referrer-Policy |
| SC-07 | Weak input validation | User fields lack bounds | Server-side validation |

## Remediation
Use parameterized SQL so input remains data. Encode untrusted HTML output. Store password hashes and verify with a password-hashing library. Require unpredictable CSRF tokens on state-changing browser requests. Disable debug in production. Add baseline browser security headers. Apply server-side length/type/format validation.

## Verification
Run:
```bash
pytest -q Task-3-Secure-Coding-Review/test_security.py
```
The tests verify XSS encoding, security headers, CSRF rejection, and normal search behavior.

## Secure coding checklist
- [x] Parameterized SQL
- [x] Output encoding
- [x] Password hashing
- [x] CSRF validation demonstration
- [x] Production-safe debug setting
- [x] Security headers
- [x] Server-side input limits
- [x] Automated regression tests
