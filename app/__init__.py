from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Instantiate Flask application
app = Flask(__name__)

# Get the values within db_config file
app.config.from_object("db_config")

db = SQLAlchemy(app)


# Load blueprint
from app import blueprint_loader

# Load error handler
from app import errorhandler_loader