#!/usr/bin/env python3
"""Module for task 4
"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)

app.url_map.strict_slashes = False


class Config:
    """Represents a Flask Babel configuration.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Determines the best match for the client's preferre
    """
    # Get the locale parameter from the incoming request
    locale = request.args.get('locale', None)
    # Get list of supported languages from Config
    supported_languages = app.config["LANGUAGES"]
    if locale and locale in supported_languages:
        # If the locale parameter is present and is a supported locale,
        # return it
        return locale
    else:
        # Use request.accept_languages to get the best match
        best_match = request.accept_languages.best_match(supported_languages)
        return best_match


@app.route("/")
def index_4() -> str:
    """The index function displays.
    """
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run(debug=True)
