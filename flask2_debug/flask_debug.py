from flask import Flask
import config     # 导入自定义的config模块

app = Flask(__name__)
app.config.from_object(config)    # config文件 与Flask实例对象app 关联


@app.route('/')
def hello_world():
    a = 1
    b = 0
    # c = a / b
    return 'Hello World! Hello Word!'


if __name__ == '__main__':
    app.run()
    # app.run(debug=True) 模式的两大功能:
    # 一是方便调试,浏览器页面输出错误信息及位置
    # 二是当内容改变时,自动更新,重启,不需要手动关闭重启
