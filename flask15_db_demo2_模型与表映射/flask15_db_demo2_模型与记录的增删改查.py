from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)

'''
sql创建article表语句:
create table article (
    id int primary key autoincrement,
    title varchar(100) not null,
    content text not null
    )
'''


class Article(db.Model):  # 模型继承自db.Model
    __tablename__ = 'article'   # 指定表名
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 创建字段对象 成为属性
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return '<Article {}>'.format(self.title)


db.create_all()   # 将模型映射到数据库中,实现创建表


@app.route('/')
def hello_world():
    # # 增加记录
    # article1 = Article(title='bbb', content='ccccccccc')
    # db.session.add(article1)
    # # 事务型处理,需要提交
    # db.session.commit()


    # 查询记录
    # 原sql语句:select * from article where article.title='aaa';
    sql = Article.query.filter(Article.title == 'aaa')   # 此句将模型的过滤转换成sql的查询语句,即quety对象
    print(sql)
    print(sql.first())   # sql对象查询不到时,返回None, 有则返回 <Article aaa>
    result = Article.query.filter(Article.title == 'bbb').all()   # result 为记录对象的列表
    print(result)    # [<Article 1>, <Article 3>]
    print(result[0].title)    # 当查询不到时,报错
    print(result[0].content)

    print(Article.query.all())  # 不过滤,查询所有记录



    # # 改记录
    # # 1.先要把更改的数据查找出来
    # article1 = Article.query.filter(Article.title == 'bbb').first()
    # # 2.把此记录对象的属性进行修改
    # article1.content = 'bbbbbbbbbb'
    # # 3.做事务提交
    # db.session.commit()



    # # 删除记录
    # # 1.先要把更改的数据查找出来
    # article1 = Article.query.filter(Article.title == 'aaa').first()
    # # 2.把这条数据删除掉
    # db.session.delete(article1)
    # # 3.做事务提交
    # db.session.commit()



    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
