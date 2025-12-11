

from flask import Flask


from flask_sqlalchemy import SQLAlchemy
# libs p login
from flask_login import LoginManager
from flask_bcrypt import Bcrypt


# lib p atualizar bd
from flask_migrate import Migrate


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///datafleshi.db"
app.config['SECRET_KEY'] = 'secret'
app.config['UPLOAD_FOLDER'] = 'static/posts_photos'


# inicializa o banco primeiro
database = SQLAlchemy(app)


# inicializa o migrate dps do banco
migrate = Migrate(app, database)


bcrypt = Bcrypt(app)
login_manager = LoginManager(app)


# direciona p onde está a tela de login (homepage no caso)
login_manager.login_view = 'homepage'


from appfleshi import routes




