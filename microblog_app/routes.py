from microblog_app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Stanley'}
    posts = [
        {
            'author': {'username':'John'},
            'body': 'Beautiful day in Vancouver!'
        },
        {
            'author': {'username':'Pikachu'},
            'body': 'Pika pika!'
        }
    ]

    return render_template('index.html', title='Home', user=user, posts=posts)
