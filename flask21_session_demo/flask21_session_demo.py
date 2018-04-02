from flask import Flask, session
import os
from datetime import timedelta

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)   # 单个配置项可以直接写入,不用写配置文件
# SECRET_KEY 是salt(盐),用来打乱原本真实的数据
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)


# 操作session时,与操作字典相同
@app.route('/<name>')
def hello_world(name):
    session['username'] = name
    # 没有指定session的过期时间,则默认为浏览器关闭结束
    session.permanent = True  # 设置永久保存为True,保存时间为配置的参数或默认30天
    return 'Hello World!'

@app.route('/get/')
def get():
    # session['username']   # 此方法不推荐,当无此key时,报错
    # session.get('username') # 推荐,无此key时,返回None
    return session.get('username')

@app.route('/delete/')
def delete():
    print(session.get('username'))
    # session.pop('username')  # 删除指定的cookie
    # del session['username']
    session.clear()  # 清除所有cookie
    print(session.get('username'))
    return 'delete cookie success!'

if __name__ == '__main__':
    app.run(debug=True)
