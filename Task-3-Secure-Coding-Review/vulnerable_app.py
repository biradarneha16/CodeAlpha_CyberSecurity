"""INTENTIONALLY VULNERABLE local training target."""
import sqlite3
from flask import Flask, request
app=Flask(__name__); DB="training.db"
def db(): return sqlite3.connect(DB)
@app.route('/search')
def search():
    term=request.args.get('q',''); conn=db()
    # VULNERABLE: input concatenated into SQL.
    rows=conn.execute("SELECT username FROM users WHERE username LIKE '%"+term+"%'").fetchall(); conn.close()
    return '<br>'.join(row[0] for row in rows)
@app.route('/hello')
def hello():
    name=request.args.get('name','guest')
    # VULNERABLE: input inserted into HTML without encoding.
    return '<h1>Hello '+name+'</h1>'
@app.route('/login',methods=['POST'])
def login():
    username=request.form.get('username',''); password=request.form.get('password',''); conn=db()
    # VULNERABLE: plaintext password comparison model.
    row=conn.execute('SELECT username FROM users WHERE username = ? AND password = ?',(username,password)).fetchone(); conn.close()
    return 'Logged in' if row else 'Invalid credentials'
@app.route('/change-email',methods=['POST'])
def change_email():
    # VULNERABLE: no CSRF token validation.
    return 'Email changed'
if __name__=='__main__': app.run(host='127.0.0.1',port=5000,debug=True)
