# coding=utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)   # app载入配置文件
db = SQLAlchemy(app)  # 创建一个db数据库对象

db.create_all()    # 测试一下


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
