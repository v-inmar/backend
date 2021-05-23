# from app import app
from app.index import app

# Register the items blueprint into the app
from app.api.items.blueprint import items_bp
app.register_blueprint(items_bp)

# Register the note blueprint into the app
from app.api.notes.blueprint import notes_bp
app.register_blueprint(notes_bp)