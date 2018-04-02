from flask import Flask
import config
from models import Article  # 这是必须要引用的
from exts import db

app = Flask(__name__)
app.config.from_object(config)
# db = SQLAlchemy(app)  # 这是原来的写法,现在是从exts.py文件中导入db
db.init_app(app)    # 在此初始化数据库

# class Article(db.Model):  # 当模型很复杂时,文件会凌乱
#     __tablename__ = 'article'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     title = db.Column(db.String(100), nullable=False)

db.create_all(bind='__all__', app=app)  # 将此app绑定到服务器app栈顶上


@app.route('/')
def hello_world():
    articel1 = Article(title='zzzz')
    db.session.add(articel1)
    db.session.commit()
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
