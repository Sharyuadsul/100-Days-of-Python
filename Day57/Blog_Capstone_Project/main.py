from flask import Flask, render_template
import requests
from post import Post

response = requests.get('https://api.npoint.io/b6d364bf213853a6ed8d')
posts =response.json()

all_posts = []
for i in posts:
    a_post_obj = Post(i['id'], i['title'], i['subtitle'], i['body'])
    all_posts.append(a_post_obj)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", all_posts = all_posts)

@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    for post in all_posts:
        if post.id == index:
            requested_post = post
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)
