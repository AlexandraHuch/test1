from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def test():
    return render_template("test.html")

@app.route("/ramen")
def ramen():
    return render_template("ramen.html")
