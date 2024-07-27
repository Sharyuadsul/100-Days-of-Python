from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return ("<h1 style='text-align:center'>Hello, World!</h1>"
            "<p>This is a paragraph</P>"
            "<img src= 'https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExYnZmbGkzeDVjcnU4a2x5cDU0enB2cjVmbzl2MDBkYWlrMmt4dGlkYyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/cXaeWuJ1oKO4g/giphy.gif'>")

def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper
@app.route("/bye")
@make_emphasis
@make_underlined
def say_bye():
    return "BYE!"

# @app.route("/<name>")
# def greet(name):
#     return f"<h1>Hello there {name + '19'}</h1>"

@app.route("/username/<name>/<int:number>")
def greet(name,number):
    return f"<h1 style='text-align:center' >Hello there {name}, You are {number} years old</h1>"


if __name__ == '__main__':
    app.run(debug=True)