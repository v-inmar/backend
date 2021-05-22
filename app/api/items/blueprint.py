from flask import Blueprint
from .read import (read_all, read_single)
from .create import create
from .update import update
from .delete import delete

# Initialize a Blueprint for the items API routes
items_bp = Blueprint(name="items", import_name=__name__, template_folder="templates", url_prefix="/items")

# Create an iteam
items_bp.add_url_rule(
    rule="",
    endpoint="create_item",
    view_func=create,
    methods=['POST']
)


# Get all items
items_bp.add_url_rule(
    rule="",
    endpoint="get_items",
    view_func=read_all,
    methods=['GET']
)

# Get an item using pid
items_bp.add_url_rule(
    rule="/<string:pid>",
    endpoint="get_item",
    view_func=read_single,
    methods=['GET']
)


# Update an item using pid
items_bp.add_url_rule(
    rule="/<string:pid>",
    endpoint="update_item",
    view_func=update,
    methods=['PUT']
)


# Delete an item using pid
items_bp.add_url_rule(
    rule="/<string:pid>",
    endpoint="delete_item",
    view_func=delete,
    methods=['DELETE']
)

