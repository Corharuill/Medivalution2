from Medievalution import app
from flask import render_template, flash, redirect
from Medievalution.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    action = ['Сражайтесь в битвах', 'Торгуйте', 'Заключайте союзы' , 'Объявляйте войны']
    return render_template('index.html', action = action )

@app.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    flash('Login requested for user {}, remember_me={}'.format(
      form.username.data, form.remember_me.data))
    return redirect('/index')
  return render_template('login.html', title='Sign In', form=form)



#Прсто html код для вывод на страницу на прямую.