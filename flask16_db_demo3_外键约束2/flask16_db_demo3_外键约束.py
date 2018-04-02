from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), nullable=False)

class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))   # 引入外键

    author = db.relationship('User', backref=db.backref('articles'))  # 正向引用,反向引用,引用到的是另一个表的记录
db.create_all()

@app.route('/')
def hello_world():

    # # 添加记录
    # user1 = User(username='chenxudong')
    # db.session.add(user1)
    #
    # article1 = Article(title='aaa', content='aaaaaaaaa')
    # article1.author = User.query.filter(User.id == 1).first()  # 另一种添加外键方式
    # db.session.add(article1)
    # db.session.commit()


    #同样要求寻找文章标题为aaa的作者
    article1 = Article.query.filter(Article.title == 'aaa').first()
    print('文章标题为aaa的作者是:%s' % article1.author.username)

    # 手动增加了几条Article记录,要求找到用户名为chenxudong写过的所有文章
    user1 = User.query.filter(User.username == 'chenxudong').first()
    result = user1.articles
    for ar in result:
        print('-'*10)
        print('文章id为{},文章标题为{}'.format(ar.id, ar.title))


    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
