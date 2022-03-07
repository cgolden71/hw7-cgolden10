import flask
from flask import Flask
from flask import jsonify
import random

app = flask.Flask(__name__)
bp = flask.Blueprint(
    "bp",
    __name__,
    template_folder="./static/react",
)
funFact = [ "Avocados are a fruit, not a vegetable.",
            "Australia is wider than the moon",
            "It's illegal to own just one guinea pig in Switzerland."]

@bp.route("/")
def index():

    return flask.render_template("index.html")

@app.route("/fun-fact")
def getFunFact():
    return jsonify(random.choice(funFact))



app.register_blueprint(bp)

app.run()
