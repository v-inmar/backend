from flask import Blueprint
from .read import (read_all, read_single)

# Initialize a Blueprint for the items API routes
items_bp = Blueprint(name="items", import_name=__name__, template_folder="templates", url_prefix="/items")

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

