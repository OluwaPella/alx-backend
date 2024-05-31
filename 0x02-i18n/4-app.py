#!/usr/bin/env python3

"""
Task1 -initialize flask app
to use babel.
"""
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)


class Config:
    """Represents a Flask Babel configuration.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale():
    """use he locale from the header
    or we support de/fr/en.
    """
    locale = request.args.get('locale')

    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def get_index():
    
    locale = get_locale()
    """
    return 2-index.html
    """

    return render_template('3-index.html')


if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0')