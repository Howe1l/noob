import os, sys
from flask import Flask, render_template
from flask import url_for
from flask_sqlalchemy import SQLAlchemy
import click

WIN = sys.platform.startswith('win')
if WIN:  # 如果是windows系统，使用三个斜线
    prefix = 'sqlite:///'
else:  # 否则使用四个斜线
    prefix = 'sqlite:////'
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(app.root_path, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #关闭对模型修改的监控

db = SQLAlchemy(app)
# @app.route('/')
# def hello():
#     return '<h1>不来一份色图吗</h1><img src="C:/Users/howe1l/Desktop/64a66e3d9ed99bd1.jpg">'

@app.route('/user/<name>')
def user_page(name):
    return 'User:%s' % name

@app.route('/text')
def tese_url_for():
    print(url_for('hello'))

    print(url_for('user_page', name='howe1l'))

    print(url_for('user_page', name='bai'))

    print(url_for('tese_url_for'))

    print(url_for('tese_url_for', num=2))

    print(url_for())

    return 'Test page'

name = "howe1l"
movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'The Pork of Music', 'year': '2012'},
]

@app.route('/')
def index():
    user = User.query.first()
    movies = Movie.query.all()
    return render_template('index.html', movies=movies)

# ------创建数据库模型--------

class User(db.Model): #表名将会是 user （自动生成，小写处理）
    id = db.Column(db.Integer, primary_key=True) #主键
    name = db.Column(db.String(20))  #名字

class Movie(db.Model): # 表名将是movie
    id = db.Column(db.Integer, primary_key=True)  #主键
    title = db.Column(db.String(60))  # 电影标题
    year = db.Column(db.String(4)) #电影年份


# ------自定义命令来自动执行创建数据库表操作------

@app.cli.command()  #注册为命令
@click.option('--drop', is_flag=True, help='Create after drop.') #设置选项
    # help突然变成了字符而不是参数，应当注意这种错误

def initdb(drop):
    """Initialize the database."""
    if drop: #判断是否输入了选项
        db.drop_all()
    db.create_all()
    click.echo('Initialized databasa.') #输出提示信息


# -----生成虚拟数据的命令函数forge----

@app.cli.command()
def forge():
    """Gennerate fake data."""
    db.create_all()

    # 全局的两个变量移动到这个函数内

    name = "howe1l"
    movies = [
        {'title': 'My Neighbor Totoro', 'year': '1988'},
        {'title': 'Dead Poets Society', 'year': '1989'},
        {'title': 'A Perfect World', 'year': '1993'},
        {'title': 'Leon', 'year': '1994'},
        {'title': 'Mahjong', 'year': '1996'},
        {'title': 'Swallowtail Butterfly', 'year': '1996'},
        {'title': 'King of Comedy', 'year': '1999'},
        {'title': 'Devils on the Doorstep', 'year': '1999'},
        {'title': 'WALL-E', 'year': '2008'},
        {'title': 'The Pork of Music', 'year': '2012'},
    ]

    user = User(name=name)
    db.session.add(user)
    for m in movies:
        movie = Movie(title=m['title'], year=m['year'])
        db.session.add(movie)

    db.session.commit()
    click.echo('Done.')

# ----404错误处理函数----

@app.errorhandler(404)  # 传入要处理的错误代码
def page_not_found(e): # 接受异常对象作为参数
    user = User.query.first()
    return render_template('404.html'), 404 #返回模版和状态码

# ----模版上下文处理函数----

@app.context_processor
def inject_user():  # 函数名可随意更改
    user = User.query.first()
    return dict(user=user)  # 需要返回字典，等同于return {'user': user}