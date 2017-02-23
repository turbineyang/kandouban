# -*-coding:utf-8 -*-
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import Required, Length, Email


class FlaskForm(Form):
    name = StringField('What is your name?', validators=[Required(), Length(1,10)])
    password = PasswordField('input your password', validators=[Required()])
    remember_me = BooleanField('记住我')
    submit = SubmitField('注册')