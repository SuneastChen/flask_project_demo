from flask import Flask, g, render_template, request
from utils import login_log

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        u = request.form.get('username')
        p = request.form.get('password')
        if u == 'chenxudong' and p == '123456':

            # 方法1:通过传参
            # login_log(u)


            # 方法2:通过全局变量g对象
            g.username = u
            g.password = p
            login_log()

            return '%s登陆成功!' % u
        else:
            return '您的用户名或密码错误!'

if __name__ == '__main__':
    app.run(debug=True)
