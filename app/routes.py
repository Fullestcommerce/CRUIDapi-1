from flask import request, jsonify
from . import db
from .models import Item
from flask import current_app as app

@app.route("/items", methods=["GET"])
def get_items():
    items = Item.query.all()
    return jsonify([item.to_dict() for item in items]), 200

@app.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    item = Item.query.get_or_404(item_id)
    return jsonify(item.to_dict()), 200

@app.route("/items", methods=["POST"])
def create_item():
    data = request.json
    item = Item(
        name=data.get("name"),
        description=data.get("description"),
        quantity=data.get("quantity", 0),
        location=data.get("location")
    )
    db.session.add(item)
    db.session.commit()
    return jsonify(item.to_dict()), 201

@app.route("/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    item = Item.query.get_or_404(item_id)
    data = request.json
    item.name = data.get("name", item.name)
    item.description = data.get("description", item.description)
    item.quantity = data.get("quantity", item.quantity)
    item.location = data.get("location", item.location)
    db.session.commit()
    return jsonify(item.to_dict()), 200

@app.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    item = Item.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return jsonify({"message": "Item deleted"}), 200
