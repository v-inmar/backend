from flask import Blueprint

from app.api.notes.create import create
from app.api.notes.read import (read_single, read_all)
from app.api.notes.update import update
from app.api.notes.delete import delete


# Initialize a Blueprint for the notes API routes
notes_bp = Blueprint(name="notes", import_name=__name__, template_folder="templates", url_prefix="/notes")

# Create a note
notes_bp.add_url_rule(
    rule="",
    endpoint="create_note",
    view_func=create,
    methods=['POST']
)

# Get all notes
notes_bp.add_url_rule(
    rule="",
    endpoint="get_notes",
    view_func=read_all,
    methods=['GET']
)

# Get an note using pid
notes_bp.add_url_rule(
    rule="/<string:pid>",
    endpoint="get_note",
    view_func=read_single,
    methods=['GET']
)

# Update a note using pid
notes_bp.add_url_rule(
    rule="/<string:pid>",
    endpoint="update_note",
    view_func=update,
    methods=['PUT']
)

# Delete a note using pid
notes_bp.add_url_rule(
    rule="/<string:pid>",
    endpoint="delete_note",
    view_func=delete,
    methods=['DELETE']
)