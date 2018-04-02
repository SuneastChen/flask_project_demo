from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)

article_tag = db.Table('article_tag',
                       db.Column('article_id', db.Integer, db.ForeignKey('article.id'), primary_key=True),
                       db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'),primary_key=True)
                       )  # 外键多对多关系,要通过中间表进行关联,不能通过"class"实现,只能通过"db.Table"方式

class Article(db.Model):
    __tabalename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)

    tags = db.relationship('Tag', secondary=article_tag, backref=db.backref('articles'))
    # 正反向引用外表记录,"secondary"参数为中间的关联表参数

class Tag(db.Model):
    __name__ = 'tag'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)

db.create_all()

@app.route('/')
def hello_world():
    # # 添加记录:
    # article1 = Article(title='aaaaa')
    # article2 = Article(title='bbbbb')
    #
    # tag1 = Tag(name='11')
    # tag2 = Tag(name='22')
    #
    # # 给"article_tag"表添加记录
    # article1.tags.append(tag1)
    # # article1对象,即title='aaaaa' 与 tag1对象,即name='11' 关联
    # article2.tags.append(tag1)
    # article2.tags.append(tag2)
    #
    # db.session.add(article1)
    # db.session.add(article2)
    # db.session.add(tag1)
    # db.session.add(tag2)
    #
    # db.session.commit()






    # 要求查询title='bbbbb'的所有标签的名字(tags.name)
    article1 = Article.query.filter(Article.title == 'bbbbb').first()
    tags_list = article1.tags
    for t in tags_list:
        print('title=bbbbb的标签是%s' % t.name)


    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
