from flask import Flask
import config
from exts import db
from models import Article

app = Flask(__name__)
app.config.from_object(config)
# db = SQLAlchemy(app)  # 这是原来的写法,现在是从exts.py文件中导入db
db.init_app(app)    # 在此初始化数据库

# db.create_all(bind='__all__', app=app)  # 用了flask_migrate就不需要这句了


@app.route('/')
def hello_world():
    articel1 = Article(title='zzzz', content='zzzzzzzzzzzz')
    db.session.add(articel1)
    db.session.commit()
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
