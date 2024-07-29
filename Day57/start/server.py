from flask import Flask, render_template
import random
import datetime
import requests


app = Flask(__name__)

@app.route('/')
def home():
    ran = random.randint(1, 10)
    year = datetime.datetime.now().year
    return render_template('index.html', num=ran, year=year)

@app.route('/guess/<string:name>')
def guess(name):
    gender_url= f'https://api.genderize.io?name={name}'
    gender_response = requests.get(gender_url)
    gender_data = gender_response.json()
    gender =gender_data['gender']

    age_response = requests.get(f'https://api.agify.io?name={name}')
    age = age_response.json()['age']
    return render_template('guess.html', name = name, gender=gender, age=age)

@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    response = requests.get('https://api.npoint.io/b6d364bf213853a6ed8d')
    my_blogs = response.json()
    return render_template('blog.html', posts = my_blogs)


if __name__ == '__main__':
    app.run(debug=True)