from flask_wtf import FlaskForm #criar forms
from wtforms import StringField, PasswordField, SubmitField, FileField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Length #importa todas partes do forms
from appfleshi.models import User #importa a tabela p conseguir ver os users

#em caso de legenda mexer aqq
class PhotoForm(FlaskForm):
    photo = FileField('Foto', validators=[DataRequired()])
    submit = SubmitField('Postar')




#criando forms - login
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Login')

#criando forms - cadastro
class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()]) #length p definir a qntd de caracteres
    username = StringField('Nome de Usuário', validators=[DataRequired(), Length(min=4, max=20)])
    password = PasswordField('Senha', validators=[DataRequired(), Length(min=6, max=60)])
    confirm_password = PasswordField('Confirmar senha', validators=[DataRequired(), EqualTo('password')]) #entende q tem q ta igual a password p funcionar
    submit = SubmitField('Criar Conta')

    #função p ver se o email q digitou já existe
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            return ValidationError("Email já cadastrado. Faça Login!")
        return None

