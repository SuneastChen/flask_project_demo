# _*_ coding:utf-8 _*_
# !/usr/bin/python
from flask_script import Manager
from flask19_分开models和解决循环引用 import app
from flask_migrate import Migrate, MigrateCommand
from exts import db
from models import Article  # 必须导入建表的模型

manager = Manager(app)

# 1.要使用flask_migrate,必须绑定app和db
migrate = Migrate(app, db)
# 2.把MigrateCommand命令(相当于集成的数据库的命令)添加到manager中
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
