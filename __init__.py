from flask import Flask, render_template, url_for, session, redirect, flash
from flask_bootstrap import Bootstrap
from form import FlaskForm
from pymongo import MongoClient

app = Flask('kandouban')
DEBUG = True
app.config['SECRET_KEY'] = 'development key'
bootstrap = Bootstrap(app)
client = MongoClient('127.0.0.1', 27017)
db = client.hello


@app.route('/', methods=['GET', 'POST'])
def index():
    form = FlaskForm()
    if form.validate_on_submit():
        user = session.get('name')
        if user is not None and user != form.name.data:
            flash('sign up successful!!')
        session['name'] = form.name.data
        session['password'] = form.password.data
        db.collec.insert({'name': session['name'],
                          'password': hash(session['password'])})
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'))


@app.route('/movie')
def movie():
    return render_template('movie_select.html')

if __name__ == '__main__':
    app.run(port=5001)
