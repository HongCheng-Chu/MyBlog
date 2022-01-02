from flask import Flask,render_template,request, url_for, redirect, flash, session
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
import json
import SQL_data
import pymssql


app=Flask(__name__)

'''
Login items


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin):
    pass

@login_manager.user_loader
def user_loader(name):
    if name not in users:
        return

    user = User()
    user.id = name
    return user


@login_manager.request_loader
def request_loader(request):

    name = request.form.get('user_id')
    if name not in users:
        return

    user = User()
    user.id = name

    user.is_authenticated = request.form['password'] == users[name]['password']

    return user
'''

'''
Web items
'''

@app.route('/', methods=['POST', 'GET'])
def init():

    with open("./girls_data.json", 'r') as f:
        girls_data = json.load(f)

    return render_template('Actresses.html', header_items = header_items, girls_card = girls_data)

'''
@app.route('/login',methods=['POST','GET'])
def login():

    if request.method == 'GET':
        return render_template('login.html')

    if request.form['send'] == 'cancel':
        return redirect(url_for('init'))

    name = request.form['user_id']
    if (name in users) and request.form['password'] == users[name]['password']:
        user = User()
        user.id = name
        login_user(user)
        return redirect(url_for('main')) # redirect: 填入def函式名稱

    return render_template('login.html')


@app.route('/main',methods=['POST'])
def main():
    if current_user.is_authenticated:
        return render_template('main.html', header_items = header_items)


@app.route('/logout', methods=['POST'])
def logout():
    logout_user()
    return redirect(url_for('init'))
'''
'''
Input items
'''

header_items = [{'name': '首頁', 'url': '#'}, 
                {'name': 'Github', 'url': 'https://github.com/HongCheng-Chu'}, 
                {'name': 'Linkedin', 'url': 'https://www.linkedin.com/in/%E5%BC%98%E6%AD%A3-%E6%9C%B1-8567961a5/'}, 
                {'name': 'Artists', 'url': '../Blog'},
                {'name': 'LeetCode', 'url': '../Blog'}]

'''
Start
'''

if __name__ == '__main__':
	app.run(host='0.0.0.0',port='5000',debug=True)