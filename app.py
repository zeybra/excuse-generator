from flask import Flask, render_template
from random import choice

app = Flask(__name__)

with open("excuses.txt") as f:
        excuses = f.read().splitlines()

@app.route("/")
def index():
    default_string = ""
    return render_template("index.html", default_string=default_string)

@app.route("/generate")
def generate():
    return choice(excuses)

if __name__ == "__main__":
    app.run()
