#!/usr/bin/env python3
"""get language from request
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """set app's language config
    """
    DEBUG = True
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """get local language from request
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """outputs hello world
    """
    return render_template("3-index.html")


if __name__ == "__main__":
    app.run()
