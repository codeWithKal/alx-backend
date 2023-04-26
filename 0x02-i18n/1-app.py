#!/usr/bin/env python3

from flask import Flask
from flask_babel import Babel

app = Flask(__name__)


class Config:
    """
    A class to be passed to app.config.from_object method
    """
    LANGUAGES = ["en", "fr"]
    BBABEL_DEFAULT_LOCAL = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

babel = Babel(app)
