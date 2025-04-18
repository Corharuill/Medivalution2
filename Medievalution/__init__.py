from flask import Flask, request
from Medievalution.config import  Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)

#инициализация пакета Медивалюэйшен

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)

from Medievalution import routes, models