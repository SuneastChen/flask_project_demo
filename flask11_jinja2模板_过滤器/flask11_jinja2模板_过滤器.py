from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    comments_list =[
        {'name': '张三', 'comment': 'xxxxxxxxxxxxxxxxxxxxxxxx'},
        {'name': '李四', 'comment': 'yyyyyyyyyyyyyyyyyyyyyyyy'},
        {'name': '王五', 'comment': 'zzzzzzzzzzzzzzzzzzzzzzzz'}
    ]

    # return render_template('index.html', img_url='http://avatar.fishc.com/avatar.php?uid=324306&size=middle')
    return render_template('index.html',comments_list=comments_list)    # 当没有传img_url参数时,则用default过滤器的默认值


if __name__ == '__main__':
    app.run(debug=True)
