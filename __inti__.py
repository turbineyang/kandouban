from flask import Flask

app = Flask(__name__)
DEBUG = True
SECRET_KEY = 'development key'

@app.route('/index/<name>')
def index(name):
    return '<h1>hello %s flask</h1>'%name

if __name__ == '__main__':
    app.run(port=5001)

