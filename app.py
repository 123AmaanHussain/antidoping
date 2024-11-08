from flask import Flask, render_template, request
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mongo"
mongo = PyMongo(app)

# @app.route("/")
# def index():
#     return f"<h1>hello</h1>"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/podcasts")
def podcasts():
    return render_template("podcasts.html")

@app.route("/antidopingwiki")
def antidopingnews():
    return render_template("antidopingwiki.html")

@app.route("/digitaltwin")
def digitaltwin():
    return render_template("digitaltwin.html")

@app.route("/caloriescalculator")
def caloriescalculator():
    return render_template("caloriescalculator.html")

@app.route("/smartlabels")
def smartlabels():
    return render_template("smartlabels.html")

@app.route("/games")
def games():
    return render_template("games.html")

# @app.route("/aboutus")
# def aboutus():
#     return render_template("aboutus.html")

if __name__ == "__main__":
    app.run(debug=True)

