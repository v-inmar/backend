from app import app

# Register the items blueprint into the app
from app.api.items.blueprint import items_bp
app.register_blueprint(items_bp)