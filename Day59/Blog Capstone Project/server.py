from flask import Flask, render_template
import requests

blog_url = 'https://api.npoint.io/a0ae3ada2e96e0311a54'
response = requests.get(blog_url)
blog_data = response.json()

app = Flask(__name__)

@app.route('/')
def get_all_posts():
    return render_template('index.html', all_posts=blog_data)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/<int:num>')
def post(num):
    requested_post = None
    for post in blog_data:
        if post['id'] == num:
            requested_post = post
    return render_template('post.html', post = requested_post)


if __name__ == '__main__':
    app.run(debug=True)