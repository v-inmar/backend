from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Instantiate Flask application
app = Flask(__name__)

# Makes the configuration values available to the app for use
app.config.from_object("key_config")
app.config.from_object("db_config")

# Instantiate a SQLAlchemy instance for the app to use
db = SQLAlchemy(app)


# Load blueprint
from app import blueprint_loader

# Load error handler
from app import errorhandler_loader