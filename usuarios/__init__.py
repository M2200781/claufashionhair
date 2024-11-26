#pip install flask-login flask-bcrypt
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import os
import sqlalchemy


app = Flask(__name__)
app.config["SECRET_KEY"] = "07d53d8079db1adde65569a4fc8b467a"

if os.getenv("DATABASE_URL"):
    pass #app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///usuarios.db"


database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

login_manager.login_view = "index"

from usuarios import models

engine = sqlalchemy.create_engine(app.config["SQLALCHEMY_DATABASE_URI"])
inspector = sqlalchemy.inspect(engine)
if not inspector.has_table("usuarios"):
    with app.app_context():
        database.drop_all()
        database.create_all()
        print('Base de dados Criado')
else:
    print('Base de dados já existe')

from usuarios import routes

