from flask import Flask, render_template
import requests
from flask import request
import smtplib

from dotenv import load_dotenv
import os
load_dotenv('../../.env')

MY_MAIL = os.getenv('MY_MAIL')
MY_PASSWORD = os.getenv('APP_PASSWORD')

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        sendmail(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

def sendmail(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP('smtp.gmail.com', port=587) as conn:
        conn.starttls()
        conn.login(MY_MAIL, MY_PASSWORD)
        conn.sendmail(MY_MAIL, MY_MAIL, email_message)




if __name__ == "__main__":
    app.run(debug=True, port=5001)
