from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    books_list = [
        {'name': '西游记', 'author': '吴承恩', 'price': 100},
        {'name': '水浒传', 'author': '施耐庵', 'price': 200},
        {'name': '三国演义', 'author': '罗贯中', 'price': 300},
        {'name': '红楼梦', 'author': '曹雪琴', 'price': 400}
    ]
    return render_template('index.html',books_list=books_list)


if __name__ == '__main__':
    app.run(debug=True)
