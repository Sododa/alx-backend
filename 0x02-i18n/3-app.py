#!/usr/bin/env python3
"""task 3
"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)

app.url_map.strict_slashes = False


class Config:
    """Represents a Flask Babel
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@app.route("/")
def index_3() -> str:
    """The index function displays the home page
    """
    return render_template("3-index.html")


@babel.localeselector
def get_locale() -> str:
    """Determines the best match for the client's preferred langua.
    """
    # Get list of supported languages from Config
    supported_languages = app.config["LANGUAGES"]
    # Use request.accept_languages to get the best match
    best_match = request.accept_languages.best_match(supported_languages)
    return best_match


if __name__ == "__main__":
    app.run(debug=True)
