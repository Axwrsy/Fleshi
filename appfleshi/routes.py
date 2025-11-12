from flask import  render_template, request
from appfleshi import app


@app.route('/')
def homepage():
    return render_template('homepage.html')

#rota dinamica nome da var
@app.route('/profile/<username>')
def profile(username):
    return render_template('profile.html', username=username)



