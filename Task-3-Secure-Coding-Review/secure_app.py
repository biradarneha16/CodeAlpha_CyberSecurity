"""Secure reference implementation for the CodeAlpha review."""
import os,secrets,sqlite3
from flask import Flask,abort,request
from markupsafe import escape
from werkzeug.security import check_password_hash
app=Flask(__name__); app.config['SECRET_KEY']=os.environ.get('SECRET_KEY',secrets.token_hex(32)); DB='secure_training.db'
def db(): return sqlite3.connect(DB)
def valid_csrf():
    expected=request.cookies.get('csrf_token'); supplied=request.form.get('csrf_token')
    return bool(expected and supplied and secrets.compare_digest(expected,supplied))
@app.get('/search')
def search():
    term=request.args.get('q','').strip()
    if len(term)>100: abort(400,'search term too long')
    conn=db(); rows=conn.execute('SELECT username FROM users WHERE username LIKE ? LIMIT 50',(f'%{term}%',)).fetchall(); conn.close()
    return '<br>'.join(escape(row[0]) for row in rows)
@app.get('/hello')
def hello():
    name=request.args.get('name','guest').strip()
    if len(name)>80: abort(400,'name too long')
    return f'<h1>Hello {escape(name)}</h1>'
@app.post('/login')
def login():
    username=request.form.get('username','').strip(); password=request.form.get('password','')
    if len(username)>80 or len(password)>256: abort(400,'invalid input')
    conn=db(); row=conn.execute('SELECT username,password_hash FROM users WHERE username = ?',(username,)).fetchone(); conn.close()
    if row and check_password_hash(row[1],password): return 'Logged in'
    return 'Invalid credentials',401
@app.post('/change-email')
def change_email():
    if not valid_csrf(): abort(403,'CSRF validation failed')
    return 'Email changed'
@app.after_request
def security_headers(response):
    response.headers['X-Content-Type-Options']='nosniff'
    response.headers['Content-Security-Policy']="default-src 'self'; object-src 'none'; base-uri 'self'"
    response.headers['Referrer-Policy']='strict-origin-when-cross-origin'
    return response
if __name__=='__main__': app.run(host='127.0.0.1',port=5000,debug=False)
