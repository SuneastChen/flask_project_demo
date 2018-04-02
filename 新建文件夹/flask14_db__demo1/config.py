# _*_ coding:utf-8 _*_
# !/usr/bin/python

DIALECT = 'mysql'
DRIVER = 'mysqldb'
USERNAME = 'root'
PASSWORD = '789789'
HOST = '127.0.0.1'
PORT = '3307'
DATABASE = 'db_demo1'
SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE)
# 固定的变量名
SQLALCHEMY_TRACK_MODIFICATIONS = False

