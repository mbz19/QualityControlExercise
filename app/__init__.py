#this is the "app/__init__.py" file, which is required for Python to treat the "app" directory as a package.

#"it says there are some python programs in the app directory, and they can be imported and used in other parts of the project"

#"and helps various files import from files in this directory"

#"it can be empty, but it is a good practice to have it in the project"



from flask import Flask

from web_app.routes.home_routes import home_routes
from web_app.routes.rps_routes import rps_routes
#from web_app.routes.book_routes import book_routes
#from web_app.routes.weather_routes import weather_routes

def create_app():
    app = Flask(__name__)
    app.register_blueprint(home_routes)
    app.register_blueprint(rps_routes)
    #app.register_blueprint(book_routes)
    #app.register_blueprint(weather_routes)
    return app