from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'f01240bee11cbfd2972b4cff'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://akshay:123456@localhost:5432/akshay'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'user.login'
login_manager.login_message_category = 'info'

from appl import views
