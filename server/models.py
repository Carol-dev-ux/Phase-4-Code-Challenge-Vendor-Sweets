from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Sweet(db.Model):
    __tablename__ = 'sweet'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    vendor_sweets = db.relationship('VendorSweet', back_populates='sweet', cascade='all, delete-orphan')

class Vendor(db.Model):
    __tablename__ = 'vendor'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    vendor_sweets = db.relationship('VendorSweet', back_populates='vendor', cascade='all, delete-orphan')

class VendorSweet(db.Model):
    __tablename__ = 'vendor_sweet'
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float, nullable=False)
    sweet_id = db.Column(db.Integer, db.ForeignKey('sweet.id'), nullable=False)
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendor.id'), nullable=False)
    sweet = db.relationship('Sweet', back_populates='vendor_sweets')
    vendor = db.relationship('Vendor', back_populates='vendor_sweets')
