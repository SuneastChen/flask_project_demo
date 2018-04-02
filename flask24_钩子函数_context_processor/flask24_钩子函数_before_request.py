from flask import Flask, session, request, render_template, g
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)


# index函数: 看g对象是否有值 --> 返回不同的数据
@app.route('/')
def index():
    if g.username:
        text = '已登陆的用户名是:%s' % g.username
    else:
        text = '未登陆...'
    print(text)
    return render_template('index.html', text=text)


# login函数: 获取用户信息 --> 数据库验证 --> 验证ok,保存session --> 返回登陆成功页面
@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        u = request.form.get('username')
        p = request.form.get('password')

        if u == 'chenxudong' and p == '123456':  # 数据库验证
        # if u == User.query.filter(User.name == u).first().username:
            session['username'] = u
            # return '登陆成功!(已保存了session信息)'
            return render_template('login_success.html')
        else:
            return '用户名或密码错误!请检查'




# 在视图函数执行之前被打劫执行,一般用于将session信息获取到,保存到g对象中,在数据库里验证下,以供其他视图函数使用
# 其他视图函数用到session信息时,就不用再获取,再从数据库中验证了
# before_request函数:获取session 给 g对象 --> 若有值,则数据库验证下,否则为空
@app.before_request
def my_before_request():
    g.username = session.get('username')
    if g.username == 'chenxudong':  # 数据库验证
        pass
    else:
        g.username = ''
    print(g.username)


# 当后台参数前台用得频繁,很多前台页面都需要此参数,这时可以context_processor(上下文处理钩子函数)
# 需要返回一个字典形式,所有的前台页面都可以用
@app.context_processor
def my_before_request():
    return {'my': '天狼集团的网站'}



if __name__ == '__main__':
    app.run(debug=True)
