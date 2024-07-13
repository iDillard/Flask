from flask import Blueprint, render_template, request, jsonify, redirect, url_for
# "Blueprint" is used to create the blueprint for views
# "render_template" is for rendering html docs as templates
# "request" is used for query parameters
# "jsonify" is used to return data in json format
# "redirect" and "url_for" is used to redirect user to a certain page

views = Blueprint(__name__, "views") # declare the blueprint for "views"

# define the route to "views" page
# this will contain the homepage
@views.route("/")
def home():
    return render_template("index.html", name='Isaiah')
    # renders the html template "index.html"
    # "name" variable can be accessed inside the template
    # a number of varibles can be passed to the template

# create a profile based off the user name
@views.route("/profile")
def profile(username): # define profile parameter username
    args = request.args # used to access query parameters
    name = args.get('name') # will give accees to that parameter if it exist
    return render_template("index.html", name=username) # will display whatever the username is 

# return Json
# converts python dictionary to json and returns it
@views.route("/json")
def get_json():
    return jsonify({'name': 'Isaiah', 'age': 26})
# will render the page in json

# return any incoming data in json format
@views.route("/data")
def get_data():
    data = request.json
    return jsonify(data)

# redirecting
@views.route("/go-to-home")
def go_to_home():
    return redirect(url_for("views.get_json")) # redirect path for returning to the desired page, "views.home"
# using get_json for testing reasons