from flask import  render_template, url_for, redirect
from flask_login import login_required, login_user, logout_user, current_user

from appfleshi import app, database, bcrypt
from appfleshi.forms import LoginForm, RegisterForm
from appfleshi.models import User, Photo

#redireciona p login
@app.route('/')
def homepage():
    login_form = LoginForm()
    return render_template('homepage.html', form=login_form)

#nova rota p cadastro
@app.route('/createaccount', methods=['GET', 'POST'])
def createaccount():
    register_form = RegisterForm()
    if register_form.validate_on_submit():
        password = bcrypt.generate_password_hash(register_form.password.data) #criptografa a senha
        user = User(username=register_form.username.data, email=register_form.email.data, password=password)#p nao armazenaar a senha pura
        database.session.add(user)
        database.session.commit()
        login_user(user, remember=True) #faz o login do user
        return redirect(url_for('profile', username=user.username)) #retorna pra função
    return render_template('createaccount.html', form=register_form)


#rota dinamica nome da var aq eh o perfil
@app.route('/profile/<username>')
@login_required
def profile(username):
    return render_template('profile.html', username=username)




