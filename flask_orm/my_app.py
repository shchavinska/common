from flask import Flask
from config import run_config
from db import db
from rooms import api_bp_rooms
from staff import api_bp_staff
from tenants import api_bp_tenants


def create_app():
    app = Flask(__name__)
    app.config.from_object(run_config())
    db.init_app(app)

    with app.app_context():
        db.create_all()
        db.session.commit()

    app.register_blueprint(api_bp_rooms)
    app.register_blueprint(api_bp_staff)
    app.register_blueprint(api_bp_tenants)

    return app


if __name__=="__main__":
    create_app().run(debug=True)
