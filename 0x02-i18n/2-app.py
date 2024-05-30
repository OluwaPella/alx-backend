#!/usr/bin/env python3

"""Task1 -initialize flask app 
to use babel.
"""
from flask import Flask, render_template, request, g
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
def get_lacale():
    """
    if the user is logged in,
    use the locale from the user settings
    """
    user = getattr(g, 'user', None)
    if user is not None:
        return user.locale
    """
    otherwise use the locale from the header
    or we support de/fr/en.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def get_index():
    """return 2-index.html.
    """
    return render_template('2-index.html')


if __name__ == "__main__":
    
    app.run(port=5000, host='0.0.0.0')