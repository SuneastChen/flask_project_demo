# 导入Flask这个类
from flask import Flask

# 初始化一个Flask对象,Flask(),需要传递一个参数__name__
# 1.方便flask框架去寻找资源
# 2.方便flask插件出现错误时,定位错误位置,如Flask-Sqlalchemy
app = Flask(__name__)


# @app.route是一个装饰器,其作用是将url与视图函数作映射
# 当访问127.0.0.1:5000/    --->   去请求hello_word()这个函数,然后将结果返回给浏览器
@app.route('/')
def hello_world():
    return 'Hello World!我是第一个flask程序'


if __name__ == '__main__':
    app.run()
    # 启动应用服务器,接受用户请求
    # while 1:
    #     listen()
