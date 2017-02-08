from flask import Flask, render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap

app = Flask('kandouban')
DEBUG = True
SECRET_KEY = 'development key'
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=5003)

