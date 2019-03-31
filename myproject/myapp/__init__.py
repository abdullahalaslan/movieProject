from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config

app= Flask(__name__)

bootstrap = Bootstrap(app)

from myapp import views