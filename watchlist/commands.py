import click

from watchlist import app, db
from watchlist.models import User, Movie

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

@app.cli.command()
@click.option('--username', prompt=True, help='The username uesd to login.')
@click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True, help='The password used to login.')
def admin(username, password):
    """Create user"""
    db.create_all()

    user = User.query.first()
    if user is not None:
        click.echo('Updating user...')
        user.username = username
        user.set_password(password)  # 设置密码
    else:
        click.echo('Creating user...')
        user = User(username=username, name='Admin')
        user.set_password(password)  #设置密码
        db.session.add(user)

    db.session.commit() # 提交数据库会话
    click.echo('Done.')
