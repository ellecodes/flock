from app import db

ROLE_USER = 0
ROLE_ADMIN = 1

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nickname = db.Column(db.String(64), nullable = True)
    email = db.Column(db.String(64), nullable = True)
    password = db.Column(db.String(64), nullable = True)
    age = db.Column(db.Integer, nullable = True)
    gender = db.Column(db.String(64), nullable = True)
    zip_code = db.Column(db.String(15), nullable = True)
    role = db.Column(db.SmallInteger, default = ROLE_USER)
    ratings = db.relationship('Rating', backref = 'author', lazy = 'dynamic')

    def __repr__(self):
        return '<User %r>' % (self.nickname)

class Company(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64))
    url = db.Column(db.String(64))
    location = db.Column(db.String(64))
    service = db.Column(db.String(64))
    industry = db.Column(db.String(64))
    ratings = db.relationship('Rating', backref = 'reader', lazy = 'dynamic')
 
    def __repr__(self):
        return '<Company %r>' % (self.name)

class Value(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64))
    ratings = db.relationship('Rating', backref = 'subject', lazy = 'dynamic')
 
    def __repr__(self):
        return '<Value %r>' % (self.name)

class Rating(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    value_id = db.Column(db.Integer, db.ForeignKey('value.id'))
    rating = db.Column(db.Integer)
 
    def __repr__(self):
        return '<Rating %r>' % (self.rating)