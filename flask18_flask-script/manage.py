# _*_ coding:utf-8 _*_
# !/usr/bin/python
from flask_script import Manager
from flask18_flask_script import app
from db_scripts import db_manager

manager = Manager(app)

@manager.command
def bark():
    print('汪汪汪...喵喵喵...')
# 进入路径,python manage.py bark 便可执行

manager.add_command('db', db_manager)
# python manage.py db init --->> '数据库初始化完成!'
# python manage.py db change --->> '数据修改成功!'

if __name__ == '__main__':
    manager.run()   # 将manager运行.run()
