from flask import Flask, render_template, url_for, session, redirect, flash
from flask_bootstrap import Bootstrap
from form import NameForm

app = Flask('kandouban')
DEBUG = True
app.config['SECRET_KEY'] = 'development key'
bootstrap = Bootstrap(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('look like your name has changed!!')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('in.html', form=form, name=session.get('name'))

if __name__ == '__main__':
    app.run(port=5000)
