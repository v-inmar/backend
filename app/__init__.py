from flask import Flask

# Instantiate Flask application
app = Flask(__name__)


# Load blueprint
from app import blueprint_loader

# Load error handler
from app import errorhandler_loader