from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/article/<iid>')  # url传参的作用:根据不同的参数,返回 相同/不同 的页面的不同的数据
def article(iid):    # iid 为传入的参数
    return '您请求的参数是%s' % iid


if __name__ == '__main__':
    app.run(debug=True)
