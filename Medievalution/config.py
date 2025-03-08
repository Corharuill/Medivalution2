import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'my_secret_key19981996'
    #код для защиты от подделки страницы
