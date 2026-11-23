from flask import Blueprint, render_template, request

home_routes = Blueprint("home_routes", __name__)


@home_routes.route("/home")
def home():
    return render_template("home.html")


@home_routes.route("/about")
def about():
    return render_template("about.html")


@home_routes.route("/hello")
def hello():
    url_params = dict(request.args)
    message = url_params.get("message", "Hello!")
    return render_template("hello.html", message=message)