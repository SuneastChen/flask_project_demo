from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def index():
    print(url_for('my_list'))     # url_for('函数名')根据视图函数返回其url  称为"反转url"
    print(url_for('article', idd='abcdef'))
    return 'Hello World!'


@app.route('/list/')
def my_list():
    return 'list'


@app.route('/article/<idd>/')
def article(idd):
    return '您请求的参数是:%s' % idd


if __name__ == '__main__':
    app.run(debug=True)
