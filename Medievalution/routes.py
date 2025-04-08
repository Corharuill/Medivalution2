from Medievalution import app
import sqlalchemy as sa
from flask import render_template, flash, redirect, request, send_from_directory, url_for
from Medievalution.forms import LoginForm, RegisterForm, ChatForm
from .models import User, Chat
from flask_sqlalchemy import SQLAlchemy
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:/// app.db'
from Medievalution import db
from flask_login import current_user, login_user,logout_user
#db = SQLAlchemy(app)

@app.route('/')
@app.route('/index')
def index():
    action = ['Сражайтесь в битвах', 'Торгуйте', 'Заключайте союзы' , 'Объявляйте войны']
    return render_template('index.html', action = action )

@app.route('/login', methods=['GET', 'POST'])
def login():
    if not current_user.is_authenticated:
        form = LoginForm()
        if form.validate_on_submit():
              user = db.session.scalar(
                  sa.select(User).where(User.username == form.username.data))
              if user is None or not user.check_password(form.password.data):
                  flash('Invalid username or password')
                  return redirect(url_for('login'))

              login_user(user, remember=form.remember_me.data)
              return redirect('/index')
        return render_template('login.html', title='Sign In', form=form)
    return "Вы уже вошли в систему"
#Прсто html код для вывод на страницу на прямую.
@app.route('/register', methods=['GET', 'POST'])
def register(r=None):
  form = RegisterForm()
  if form.validate_on_submit():
    username=form.username.data
    password = form.password.data
    email = form.email.data
    print(username,  password, email)
    user = User(username= username, email = email)
    user.set_password(password)
    try:
        db.session.add(user)
        print(user)
        db.session.commit()
        print(user)
        return redirect('/index')

    except:
        return "При добавлении пользователя произошла ошибка"
    print(username)
    flash('Login requested for user {}, remember_me={}'.format(
      form.username.data, form.remember_me.data))
    return redirect('/index')
  return render_template('regis.html', title='Sign In', form=form)

@app.route('/download')
def download_file():
    """ Функция для скачивания файла """
    return send_from_directory(app.config['UPLOAD_FOLDER'], 'Medievalution.zip', as_attachment=True)


@app.route('/updates')
def updates():
    return render_template("updates.html")
if __name__ == "__main__":
    app.run(debug=True)


@app.route('/informatio')
def informatio():
    return render_template("informatio.html")
if __name__ == "__main__":
    app.run(debug=True)


@app.route('/chat', methods=['GET', 'POST'])
def chat():
    form = ChatForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        subject =  form.subject.data
        message = form.message.data
        print(username, subject, email, message)
        chat = Chat(username=username, email=email,subject = subject,message =message)

        print(username)
        #flash('Login requested for user {}, remember_me={}'.format(
            #form.username.data, form.remember_me.data))
        return redirect('/chat')
    return render_template('chat.html', title='Sign In', form=form)

    return render_template("chat.html")
if __name__ == "__main__":
    app.run(debug=True)

