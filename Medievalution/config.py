import os
basedir = os.path.abspath(os.path.dirname(__file__))
#определение дериктори бейзд дир

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'my_secret_key19981996'
    #код для защиты от подделки страницы

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    UPLOAD_FOLDER = 'static/uploads'

#указываем где хранится база данных
