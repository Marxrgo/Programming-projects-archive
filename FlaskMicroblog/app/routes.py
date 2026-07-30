from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Mar'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'Samuel'},
            'body': 'I love Flask!'
        },
        {
            'author': {'username': 'Scott'},
            'body': 'Maryland is the greatest!'
        },
        {
            'author': {'username': 'Jean'},
            'body': 'Beautiful day in FL!'
        },
]

    return render_template('index.html', title = 'home', user = user, posts = posts)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {form.username.data}, remeber_me={form.remember_me.data}')
        return redirect('/index')

    return render_template('login.html', title = 'Sign in', form=form)