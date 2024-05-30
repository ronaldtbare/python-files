# This is a simple flask test for a simple website

from flask import Flask

app = Flask(__name__)

@app.route("/")

def index():
    return "This a a simple Flask website!"

app.run(host="0.0.0.0", port=80)

