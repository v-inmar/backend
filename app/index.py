from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Instantiate Flask application
app = Flask(__name__)

# Makes the configuration values available to the app for use
app.config.from_object("key_config")
app.config.from_object("db_config")

# Instantiate a SQLAlchemy instance for the app to use
db = SQLAlchemy(app)

# Instantiate Flask Migrate instance for db migration
migrate = Migrate(app, db)

# Load blueprint
from app import blueprint_loader

# Load error handler
from app import errorhandler_loader

# Load orm models
from app import model_loader