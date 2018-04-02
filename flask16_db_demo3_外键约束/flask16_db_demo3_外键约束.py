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
    # password = db.Column(db.String(20), nullable=False) 只会映射一次,建表头,后续修改会报错,后加的映射语句会报错

class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))   # 引入外键
db.create_all()

@app.route('/')
def hello_world():

    # # 添加记录
    # user1 = User(username='zhiliao')
    # db.session.add(user1)
    #
    # article1 = Article(title='aaa', content='aaaaaaaaaaa', author_id=1)
    # db.session.add(article1)
    #
    # db.session.commit()  # 两条记录一起提交

    # 要求查找文章标题为aaa的这个作者
    artile1 = Article.query.filter(Article.title == 'aaa').first()
    author_id1 = artile1.author_id
    user1 = User.query.filter(User.id == author_id1).first()  # user1 是条记录对象
    print('文章标题为aaa的这个作者是:%s' % user1.username)



    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
