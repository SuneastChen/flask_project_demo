from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search/')
def search():
    print(request.args)  # 得到字典的列表 --> [('q', 'hello'), ('a', 'world')]
    q = request.args.get('q')
    a = request.args.get('a')
    return '传入的q参数的值为%s,传入的a参数为%s' % (q, a)

# 视图函数默认为GET请求,若想以POST方式,需指明
@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        u = request.form.get('username')
        p = request.form.get('password')
        return 'post方式提交数据成功! <br> 用户名为:%s,密码为:%s' % (u, p)

if __name__ == '__main__':
    app.run(debug=True)
