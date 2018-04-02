from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    dict1 = {'姓名': '老王',
             '性别': '男',
             '年龄': '30',
             '身高': 180,
             '体重': '75kg'
    }
    list1 = ['abc', 123, [1, 2, 3], {}]
    return render_template('index.html', dict=dict1, list=list1)


if __name__ == '__main__':
    app.run(debug=True)
