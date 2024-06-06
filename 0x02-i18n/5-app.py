#!/usr/bin/env python3

"""
Task1 -initialize flask app
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

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user() -> dict:
    """
    get the user
    """
    login_as_id = request.args.get('login_as')
    if login_as_id:
        return users.get(int(login_as_id))
    return None

@app.before_request      
def before_request():
    """
    feches user information before each request 
    """
    g.user = get_user()

@babel.localeselector
def get_locale():
    """
    use he locale from the header
    or we support de/fr/en.
    """
    locale = request.args.get('locale')
    supported_locale = app.config['LANGUAGES']
    if locale and locale in supported_locale:
        return locale
    return request.accept_languages.best_match(supported_locale)



@app.route('/')
def get_index():
    """
    return 2-index.html.

    """
    locale = get_locale()
    return render_template('3-index.html', locale=locale)


if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0')
