from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    class Person(object):
        def __init__(self, name, age):
            self.name = name
            self.age = age
    p = Person('黄勇', 18)

    context={
        'username': '老王',
        'gender': '男',
        'age': 52,
        'man': p,    # man是形参 代表一个实例化的Person
        'url_dict': {'baidu': 'www.baidu.com', 'Google': 'www.google.com'}  # url_dict是形参 代表一个字典
    }
    return render_template('another/index.html', **context)

if __name__ == '__main__':
    app.run(debug=True)
