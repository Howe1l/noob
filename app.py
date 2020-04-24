from flask import Flask, render_template
from flask import url_for
app = Flask(__name__)

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
    return render_template('index.html', name=name, movies=movies)