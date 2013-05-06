from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, lm, oid, models
from forms import LoginForm, EditForm, AddCoForm, RateCoForm
from models import User, ROLE_USER, ROLE_ADMIN, Company, Rating
from datetime import datetime

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.route('/')
@app.route('/index')
@login_required
def index():
    user = g.user
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
@oid.loginhandler
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        return oid.try_login(form.openid.data, ask_for = ['nickname', 'email'])
    return render_template('login.html', 
        title = 'Sign In',
        form = form,
        providers = app.config['OPENID_PROVIDERS'])

@oid.after_login
def after_login(resp):
    if resp.email is None or resp.email == "":
        flash('Invalid login. Please try again.')
        redirect(url_for('login'))
    user = User.query.filter_by(email = resp.email).first()
    if user is None:
        nickname = resp.nickname
        if nickname is None or nickname == "":
            nickname = resp.email.split('@')[0]
        user = User(nickname = nickname, email = resp.email, role = ROLE_USER)
        db.session.add(user)
        db.session.commit()
    remember_me = False
    if 'remember_me' in session:
        remember_me = session['remember_me']
        session.pop('remember_me', None)
    login_user(user, remember = remember_me)
    return redirect(request.args.get('next') or url_for('index'))

@app.before_request
def before_request():
    g.user = current_user
    if g.user.is_authenticated():
        g.user.last_seen = datetime.utcnow()
        db.session.add(g.user)
        db.session.commit()

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/user/<nickname>')
# @login_required
def user(nickname):
    user = User.query.filter_by(nickname = nickname).first()
    if user == None:
        flash('User ' + nickname + ' not found.')
        return redirect(url_for('index'))
    posts = [
        { 'author': user, 'body': 'Test post #1' },
        { 'author': user, 'body': 'Test post #2' }
    ]
    return render_template('user.html',
        user = user,
        posts = posts)

@app.route('/edit', methods = ['GET', 'POST'])
# @login_required
def edit():
    form = EditForm()
    if form.validate_on_submit():
        g.user.nickname = form.nickname.data
        g.user.age = form.age.data
        g.user.gender = form.gender.data
        g.user.location = form.location.data
        g.user.about_me = form.about_me.data
        db.session.add(g.user)
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('edit'))
    else:
        form.nickname.data = g.user.nickname
        form.age.data = g.user.age
        form.gender.data = g.user.gender
        form.location.data = g.user.location
        form.about_me.data = g.user.about_me
    return render_template('edit.html',
        form = form)

@app.route("/companies")
# @login_required
def colists():
    companies = models.Company.query.all()
    return render_template("colist.html", companies=companies)

@app.route('/company/<id>')
# @login_required
def company(id):
    company = Company.query.filter_by(id = id).first()
    if company == None:
        flash('Company ' + id + ' not found.')
        return redirect(url_for('index'))
    return render_template('company.html',
        company = company)

@app.route('/company_add', methods = ['GET', 'POST'])
# @login_required
def company_add():
    form = AddCoForm()
    if form.validate_on_submit():
        newco = Company(name = form.name.data, url = form.url.data, location = form.location.data, service = form.service.data, industry = form.industry.data)
        db.session.add(newco)
        db.session.commit()
        flash('Company has been added.')
        return redirect(url_for('colists'))
    return render_template('company_add.html',
        form = form)

@app.route('/rating', methods = ['GET', 'POST'])
# @login_required
def rating():
    form = RateCoForm()
    if form.validate_on_submit():
        # g.user.ratings.company_id = form.company_id.data
        # g.user.ratings.user_id = form.user_id.data
        g.user.ratings.WFH = form.WFH.data
        g.user.ratings.PTO = form.PTO.data
        g.user.ratings.Benefits = form.Benefits.data
        g.user.ratings.Collaboration = form.Collaboration.data
        db.session.add(g.user.ratings)
        db.session.commit()
        flash('Your ratings have been saved.')
        return redirect(url_for('rating')) 
    else:
        # form.company_id.data = g.user.ratings.company_id
        # form.user_id.data = g.user.ratings.user_id
        form.WFH.data = g.user.ratings.WFH
        form.PTO.data = g.user.ratings.PTO
        form.Benefits.data = g.user.ratings.Benefits
        form.Collaboration.data = g.user.ratings.Collaboration
    return render_template('rating.html', #change edit
        form = form)


# @app.errorhandler(404)
# def internal_error(error):
#     return render_template('404.html'), 404

# @app.errorhandler(500)
# def internal_error(error):
#     db.session.rollback()
#     return render_template('500.html'), 500

@app.route("/users")
def userslist():
    users = models.User.query.all()
    return render_template("user_list.html", users=users)

@app.route("/companies")
def colists():
    companies = models.Company.query.all()
    return render_template("colist.html", companies=companies)


# @app.route("/join")
# def create_user():
#     form = LoginForm()
#     return render_template("join.html", user_name="chriszf", form = form)

# @app.route("/company-search")
# def search_company():
#     form = LoginForm()
#     return render_template("company_search.html", user_name="chriszf", form = form)

# @app.route("/company-add")
# def add_company():  
#     form = LoginForm()
#     return render_template("company_add.html", user_name="chriszf", form = form)

# @app.route("/company-rate")
# def rate_company():
#     form = LoginForm()
#     return render_template("company_rate.html", user_name="chriszf", form = form)

# @app.route("/home")
# def home_user():
#     form = LoginForm()
#     return render_template("user_home.html", user_name="chriszf", form = form)