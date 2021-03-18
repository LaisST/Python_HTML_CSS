from flask import Flask

app = Flask("Microblog")

@app.route("/")
def index():
    return "Hello World!"

app.run()