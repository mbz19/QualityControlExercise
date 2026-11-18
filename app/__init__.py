#this is the "app/__init__.py" file, which is required for Python to treat the "app" directory as a package.

#"it says there are some python programs in the app directory, and they can be imported and used in other parts of the project"

#"and helps various files import from files in this directory"

#"it can be empty, but it is a good practice to have it in the project"


from flask import Flask

from web_app.routes import main_routes

def create_app():
    app = Flask(__name__)
    app.register_blueprint(main_routes)
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)