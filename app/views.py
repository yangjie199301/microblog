from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': '萌萌登' } # 测试用户
    posts = [ # 测试数据
        {
            'author': { 'nickname': '渣科' },
            'body': '你见过凌晨3点的洛杉矶吗!'
        },
        {
            'author': { 'nickname': '傻库' },
            'body': '只有我最沙雕!'
        }
    ]
    return render_template("index.html",
        title = 'Home',
        user = user,
        posts = posts)