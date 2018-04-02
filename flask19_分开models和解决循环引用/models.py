# _*_ coding:utf-8 _*_
# !/usr/bin/python
# from flask19_分开models和解决循环引用 import db
#  导致了循环引用,报错,解决办法:将db放到另一文件中exts.py
from exts import db

class Article(db.Model):  # 当模型很复杂时,文件会凌乱
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
