from app import app
from flask import render_template


@app.route("/")
@app.route("/index")
def index():
    user = {'username': 'Lais'}
    posts = [
        {"author": {"username": "Maria"}, "body": "Olá Lais"},
        {"author": {"username": "Lais"}, "body": "Olá Maria"}
    ]
    return render_template("index.html", user=user, posts=posts) 