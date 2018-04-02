from flask import Flask, url_for, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return '这是一个首页'


@app.route('/<user>/')
def log_success(user):
    login_url = url_for('login')
    if user == 'abc':
        return 'Hello World!登陆成功,这是登陆成功页面'
    else:
        return redirect(login_url)     # 当不符合条件时,页面跳转到其也页面


@app.route('/login/')
def login():
    return '这是一个登陆页面'

if __name__ == '__main__':
    app.run(debug=True)
