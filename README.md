# Launching with Flask
This will serve as a tutorial/descripition of how I launch a simple application with Flask

Flask is a web framework that allows developers to a build lightweight applications quickly and easily using python and the libraries provided by Flask. Flask is also capable of working with the template engine Jinja.

### Before You Begin
Flask works with Python so you will need to make sure that you have the latest verison of python installed. On windows you can check your version using the following command.

```sh
python --version
```

Next you will need to create a project folder and set up the enviroment. This can be done through file explorer or through CLI

```sh
> mkdir myproject
> cd myproject
```
Within your new project you will need to install Flask

```sh
pip install Flask
```

### Step 1
Within this project folder you will need to create two new python files.

```sh
app.py
views.py 
```
You will also create folder that will contain any templates and any other HTML. The folder has to be named "templates".
The templates folder is where your HTML will be kept.

