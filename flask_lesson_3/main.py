
from flask import Flask
from config import run_config
from rooms import api_bp_rooms
from tenants import api_bp_tenants
from staff import api_bp_staff


app = Flask(__name__)


app.register_blueprint(api_bp_rooms)
app.register_blueprint(api_bp_tenants)
app.register_blueprint(api_bp_staff)


app.config.from_object(run_config())


if __name__ == "__main__":
    app.run()

