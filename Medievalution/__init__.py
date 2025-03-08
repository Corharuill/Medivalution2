from flask import Flask
from Medievalution.config import  Config
app = Flask(__name__)
app.config.from_object(Config)
from Medievalution import routes

#инициализация пакета Медивалюэйшен

