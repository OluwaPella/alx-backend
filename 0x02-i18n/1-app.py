#!/usr/bin/env python3
"""
tasks for flask app
"""

from flask import Flask, render_template
from babel import Babel

app = Flask(__name__)

class Config:
    """Represents a Flask Babel configuration.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)

@app.route('/')
def get_index():
    """return index.html
    """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0')