from flask import Blueprint, jsonify, request
from models import db, Sweet, Vendor, VendorSweet

routes = Blueprint('routes', __name__)

# GET /vendors
@routes.route('/vendors')
def get_vendors():
    vendors = Vendor.query.all()
    vendors_list = [{'id': vendor.id, 'name': vendor.name} for vendor in vendors]
    return jsonify(vendors_list)

# GET /vendors/<int:id>
@routes.route('/vendors/<int:id>')
def get_vendor(id):
    vendor = Vendor.query.get(id)
    if vendor:
        vendor_data = {
            'id': vendor.id,
            'name': vendor.name,
            'vendor_sweets': [{
                'id': vs.id,
                'price': vs.price,
                'sweet': {'id': vs.sweet.id, 'name': vs.sweet.name},
                'sweet_id': vs.sweet_id,
                'vendor_id': vs.vendor_id
            } for vs in vendor.vendor_sweets]
        }
        return jsonify(vendor_data)
    else:
        return jsonify({'error': 'Vendor not found'}), 404

# GET /sweets
@routes.route('/sweets')
def get_sweets():
    sweets = Sweet.query.all()
    sweets_list = [{'id': sweet.id, 'name': sweet.name} for sweet in sweets]
    return jsonify(sweets_list)

# GET /sweets/<int:id>
@routes.route('/sweets/<int:id>')
def get_sweet(id):
    sweet = Sweet.query.get(id)
    if sweet:
        sweet_data = {'id': sweet.id, 'name': sweet.name}
        return jsonify(sweet_data)
    else:
        return jsonify({'error': 'Sweet not found'}), 404

# POST /vendor_sweets
@routes.route('/vendor_sweets', methods=['POST'])
def create_vendor_sweet():
    data = request.json
    price = data.get('price')
    vendor_id = data.get('vendor_id')
    sweet_id = data.get('sweet_id')

    if price is None or price < 0:
        return jsonify({'errors': ['validation errors']}), 400

    vendor = Vendor.query.get(vendor_id)
    sweet = Sweet.query.get(sweet_id)

    if vendor and sweet:
        vendor_sweet = VendorSweet(price=price, sweet_id=sweet_id, vendor_id=vendor_id)
        db.session.add(vendor_sweet)
        db.session.commit()
        response_data = {
            'id': vendor_sweet.id,
            'price': vendor_sweet.price,
            'sweet': {'id': sweet.id, 'name': sweet.name},
            'sweet_id': sweet_id,
            'vendor': {'id': vendor.id, 'name': vendor.name},
            'vendor_id': vendor_id
        }
        return jsonify(response_data), 201
    else:
        return jsonify({'errors': ['Vendor or Sweet not found']}), 404

# DELETE /vendor_sweets/<int:id>
@routes.route('/vendor_sweets/<int:id>', methods=['DELETE'])
def delete_vendor_sweet(id):
    vendor_sweet = VendorSweet.query.get(id)
    if vendor_sweet:
        db.session.delete(vendor_sweet)
        db.session.commit()
        return jsonify({}), 204
    else:
        return jsonify({'error': 'VendorSweet not found'}), 404
