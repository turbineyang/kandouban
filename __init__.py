from flask import Flask, render_template, url_for, session, redirect, flash
from flask_bootstrap import Bootstrap
from form import FlaskForm
from pymongo import MongoClient

app = Flask('kandouban')
DEBUG = True
app.config['SECRET_KEY'] = 'development key'
bootstrap = Bootstrap(app)
client = MongoClient('127.0.0.1', 27017)
db = client.douban


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = FlaskForm()
    if form.validate_on_submit():
        user = session.get('name')
        if user is not None and user != form.name.data:
            flash('sign up successful!!')
        session['name'] = form.name.data
        session['password'] = form.password.data
        db.collec.insert({'name': session['name'],
                          'password': hash(session['password'])})
        return redirect(url_for('login'))
    return render_template('login.html', form=form, name=session.get('name'))


@app.route('/')
def movie():
    text = '-'
    results = db.movie.find({"评分": {"$gt": '9.5'}})
    text = '-'
    item = map(lambda a: a['电影名'], results)
    movie_abstract = text.join(item)
    return render_template('movie.html', movie_abstract=movie_abstract)

if __name__ == '__main__':
    app.run(port=5006)
