#this is the "app/__init__.py" file, which is required for Python to treat the "app" directory as a package.

#"it says there are some python programs in the app directory, and they can be imported and used in other parts of the project"

#"and helps various files import from files in this directory"

#"it can be empty, but it is a good practice to have it in the project"



import os
from flask import Flask
from web_app.routes.home_routes import home_routes
from web_app.routes.rps_routes import rps_routes

TEMPLATE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "web_app", "templates")
)

def create_app():
    app = Flask(__name__, template_folder=TEMPLATE_DIR)
    app.register_blueprint(home_routes)
    app.register_blueprint(rps_routes)
    return app