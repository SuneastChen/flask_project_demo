# _*_ coding:utf-8 _*_
# !/usr/bin/python
from flask_script import Manager

db_manager = Manager()

@db_manager.command
def init():
    print('数据库初始化完成!')

@db_manager.command
def change():
    print('数据修改成功!')