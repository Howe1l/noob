from flask import Flask
from flask import url_for
app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>不来一份色图吗</h1><img src="C:/Users/howe1l/Desktop/64a66e3d9ed99bd1.jpg">'

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
