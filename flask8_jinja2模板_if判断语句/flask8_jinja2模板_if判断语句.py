from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<is_login>/')
def index(is_login):
    if is_login == 'cxd':
        user1 = {'username': '陈旭东', 'age': 25}
        return render_template('index.html', user=user1)
    else:
        return render_template('index.html')
    # 前台传入后台is_login参数 ---> 后台根据值作处理 ---> 后台传参user 给前台,值为user1

if __name__ == '__main__':
    app.run(debug=True)
