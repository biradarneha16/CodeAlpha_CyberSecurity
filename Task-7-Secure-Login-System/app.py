"""Demo secure login app: Flask, SQLite parameterized queries, Werkzeug password hashing."""
import os, sqlite3
from functools import wraps
from flask import Flask, request, redirect, session, url_for, render_template_string, flash
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY")
if not app.secret_key:
    raise RuntimeError("Set FLASK_SECRET_KEY to a long random secret before running.")
DB = os.environ.get("LOGIN_DB", "users.db")
PAGE = """<!doctype html><title>Secure Login Demo</title>
<h1>Secure Login Demo</h1>{% with msgs=get_flashed_messages() %}{% for m in msgs %}<p>{{m}}</p>{% endfor %}{% endwith %}
{% if user %}<p>Signed in as {{user}}</p><form method=post action=/logout><button>Logout</button></form>
{% else %}<h2>Register</h2><form method=post action=/register><input name=username minlength=3 maxlength=40 required><input name=password type=password minlength=12 required><button>Register</button></form>
<h2>Login</h2><form method=post action=/login><input name=username required><input name=password type=password required><button>Login</button></form>{% endif %}"""

def connect():
    c = sqlite3.connect(DB)
    c.row_factory = sqlite3.Row
    return c

def init_db():
    with connect() as c:
        c.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT UNIQUE NOT NULL, password_hash TEXT NOT NULL)")

@app.after_request
def security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Referrer-Policy"] = "same-origin"
    response.headers["Cache-Control"] = "no-store"
    return response

@app.get("/")
def index():
    return render_template_string(PAGE, user=session.get("username"))

@app.post("/register")
def register():
    username, password = request.form.get("username","").strip(), request.form.get("password","")
    if not (3 <= len(username) <= 40) or len(password) < 12:
        flash("Username must be 3–40 characters and password at least 12 characters."); return redirect(url_for("index"))
    try:
        with connect() as c:
            c.execute("INSERT INTO users(username,password_hash) VALUES (?,?)", (username, generate_password_hash(password, method="scrypt")))
        flash("Registration successful. Please log in.")
    except sqlite3.IntegrityError:
        flash("Unable to register that username.")
    return redirect(url_for("index"))

@app.post("/login")
def login():
    username, password = request.form.get("username","").strip(), request.form.get("password","")
    with connect() as c: user = c.execute("SELECT username,password_hash FROM users WHERE username = ?", (username,)).fetchone()
    if not user or not check_password_hash(user["password_hash"], password):
        flash("Invalid username or password."); return redirect(url_for("index"))
    session.clear()
    session["username"] = user["username"]
    session.permanent = False
    return redirect(url_for("index"))

@app.post("/logout")
def logout():
    session.clear()
    flash("You have been logged out.")
    return redirect(url_for("index"))

if __name__ == "__main__":
    init_db()
    app.run(host="127.0.0.1", port=5000, debug=False)
