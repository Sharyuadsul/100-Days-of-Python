from flask import Flask
import random

num = random.randint(0,9)
print(num)

app = Flask(__name__)

@app.route('/')
def home():
    return ('<h1>Guess a number between 0 and 9</h1>'
            '<img src = "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExNG9yanZyc3NibGRhcnF2dzY2OXhzNDlha2xqdGw3azJlZGRrNTdpdyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7aCSPqXE5C6T8tBC/giphy.gif">')

@app.route('/<int:number>')
def num_check(number):
    if number<num:
        return ("<h1 style='color: red'>Too Low..Try Again</h1>"
                "<img src = 'https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExdmJ2YzdpdGppY2R6a2Z5NzJ1cnJ0enowb2YyMTg1a2sxNDhnY3FkaSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/jD4DwBtqPXRXa/giphy-downsized-large.gif' >")

    elif number>num:
        return ("<h1 style='color: purple'>Too High..Try Again</h1>"
                "<img src = 'https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExbW9mN2g2cHd1cDc0NTY3cHBmdWIwaGF6eHVicHA4bXRrenc3aWN4eCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o6ZtaO9BZHcOjmErm/giphy.gif' >")

    else:
        return ("<h1 style='color: green'>You Found Me!!</h1>"
                "<img src = 'https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExZGZkd3FpZDU5dWxlODFnMXN5ZGJxdDF5eWlsbzNnM2Frcm82dnhnMyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/4T7e4DmcrP9du/giphy.gif'>")


if __name__=="__main__":
    app.run(debug=True)