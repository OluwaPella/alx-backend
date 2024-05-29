#!/usr/bin/env python3
"""
tasks for flask app
"""
from flask import Flask, render_template
from babel import Babel

class config:
    """Represents a Flask Babel configuration.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(config)
babel = Babel(app)

@app.route('/')
def get_index():
    """return index.html
    """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0')