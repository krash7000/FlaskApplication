from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "Set_Key_to_complex_key"



@app.route("/home")
def index():
    return render_template("index.html")

@app.route("/multiplication", methods=["POST", "GET"])
def multiplication():
    return render_template("multiplication.html")

@app.route("/division", methods=["POST", "GET"])
def division():
    return render_template("index.html")

@app.route("/addition", methods=["POST", "GET"])
def addition():
    return render_template("index.html")

@app.route("/subtraction", methods=["POST", "GET"])
def subtraction():
    return render_template("index.html")

@app.route("/store", methods=["POST", "GET"])
def store():
    return render_template("index.html")

@app.route("/stats", methods=["POST", "GET"])
def stats():
    return render_template("index.html")

