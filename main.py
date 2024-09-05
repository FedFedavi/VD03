import flask
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def acc():
    return render_template("index.html")

@app.route("/cart/")
def cart():
    return render_template("index1.html")

if __name__ == "__main__":
    app.run()

