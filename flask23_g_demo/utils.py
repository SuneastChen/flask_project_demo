# _*_ coding:utf-8 _*_
# !/usr/bin/python
from datetime import datetime
from flask import g

# # 方法1:通过传参
# def login_log(username):
#     print('当前登陆用户是{},登陆时间是{}'.format(username, datetime.today()))


# 方法2:通过全局变量g对象
def login_log():
    print('当前登陆用户是{},登陆时间是{}'.format(g.username, datetime.today()))