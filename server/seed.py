from app import create_app
from models import db, Sweet, Vendor, VendorSweet

def seed_database():
    app = create_app()

    with app.app_context():
        # Create tables
        db.create_all()

        chocolate_chip_cookie = Sweet(name='Chocolate Chip Cookie')
        brownie = Sweet(name='Brownie')
        mms_cookie = Sweet(name='M&Ms Cookie')

        insomnia_cookies = Vendor(name='Insomnia Cookies')
        cookies_cream = Vendor(name='Cookies Cream')

        db.session.add_all([chocolate_chip_cookie, brownie, mms_cookie, insomnia_cookies, cookies_cream])
        db.session.commit()

        vendor_sweets_data = [
            {'price': 45, 'vendor': insomnia_cookies, 'sweet': chocolate_chip_cookie},
            {'price': 50, 'vendor': cookies_cream, 'sweet': brownie},
            {'price': 60, 'vendor': insomnia_cookies, 'sweet': mms_cookie}
        ]

        for data in vendor_sweets_data:
            vendor_sweet = VendorSweet(price=data['price'], vendor=data['vendor'], sweet=data['sweet'])
            db.session.add(vendor_sweet)

        db.session.commit()

        print("Database seeded successfully!")

if __name__ == "__main__":
    seed_database()
