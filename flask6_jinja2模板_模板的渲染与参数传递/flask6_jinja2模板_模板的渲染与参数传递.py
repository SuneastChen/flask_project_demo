from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    # return render_template('index.html', username='陈旭东', gender='男', age=25)
    # 当有很多参数时,这样写不方便,所以用字典context存放参数,**context打散传参

    context={
        'username': '老王',
        'gender': '男',
        'age': 52
    }
    return render_template('index.html', **context)

if __name__ == '__main__':
    app.run(debug=True)
