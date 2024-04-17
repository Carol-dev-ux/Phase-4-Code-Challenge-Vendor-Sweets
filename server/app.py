from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes import routes
from models import db

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    app.register_blueprint(routes)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True,port=5005)
