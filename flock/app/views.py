from flask import render_template, flash, redirect
from app import app
from forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'Saydz!' }
    posts = [
        { 
            'author': { 'nickname': 'John' }, 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': { 'nickname': 'Susan' }, 
            'body': 'The Avengers movie was so cool!' 
        }
    ]
    return render_template('index.html',
        title = 'Home',
        user = user,
        posts = posts)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', 
        title = 'Sign In',
        form = form,
        providers = app.config['OPENID_PROVIDERS'])


# @app.route("/login")
# def index():
#     form = LoginForm()
#     return render_template("index_login.html", user_name="chriszf", form = form)

@app.route("/join-create")
def join_create_user():
    form = LoginForm()
    return render_template("user_join_create.html", user_name="chriszf", form = form)

@app.route("/company-search")
def search_company():
    form = LoginForm()
    return render_template("company_search.html", user_name="chriszf", form = form)

@app.route("/company-add")
def add_company():  
    form = LoginForm()
    return render_template("company_add.html", user_name="chriszf", form = form)

@app.route("/company-rate")
def rate_company():
    form = LoginForm()
    return render_template("company_rate.html", user_name="chriszf", form = form)

@app.route("/home")
def home_user():
    form = LoginForm()
    return render_template("user_home.html", user_name="chriszf", form = form)