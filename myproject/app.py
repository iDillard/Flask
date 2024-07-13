from flask import Flask
from views import views

# Name for the application
app = Flask(__name__)
app.register_blueprint(views, url_prefix="/") # blueprint for "views"

# Needed to run the program
# debug will auto update site upon saves'
# port number can be anything 
if __name__ == '__main__':
    app.run(debug=True, port=8000)



