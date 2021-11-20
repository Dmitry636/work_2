# -*- coding: utf-8 -*-
from flask import render_template
from app import app

student = 'Dmitry'
@app.route('/')
@app.route('/index')
def index():
    user = {'username': student}
    posts = [
        {
            'author': {'username': 'Vasya'},
            'body': 'Hello'
        },
        {
            'author': {'username': 'Petr'},
            'body': 'пРИВТ)))'
        },
        {
            'author': {'username': 'Николай'},
            'body': 'Как дела?'
        },
        {
            'author': {'username': 'Ибрагим'},
            'body': 'вась ты где?'
        },
        {
            'author': {'username': 'Глеб'},
            'body': 'Я уехал в италию'
        },
        {
            'author': {'username': 'Никита'},
            'body': 'Ptivet'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
