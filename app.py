from flask import Flask, url_for, redirect, render_template, request

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('homepage.html')

#rota dinamica nome da var
@app.route('/profile/<username>')
def profile(username):
    return render_template('profile.html', username=username)








if __name__ == '__main__':
    app.run(debug=True)
