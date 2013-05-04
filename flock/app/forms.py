from flask.ext.wtf import Form, TextField, BooleanField, TextAreaField
from flask.ext.wtf import Required, Length, NumberRange

class LoginForm(Form):
    openid = TextField('openid', validators = [Required()])
    remember_me = BooleanField('remember_me', default = False)

class EditForm(Form):
    nickname = TextField('nickname', validators = [Required()])
    age = TextField('age', validators = [])
    gender = TextField('gender', validators = [])
    location = TextField('location', validators = [])
    about_me = TextAreaField('about_me', validators = [Length(min = 0, max = 140)])

class CreateCoForm(Form):
    name = TextField('name', validators = [Required()])
    url = TextField('url', validators = [Required()])
    location = TextField('location', validators = [Required()])
    service = TextField('service', validators = [Required()])
    industry = TextField('industry', validators = [Required()])

class RateCoForm(Form):
    WFH = TextField('WFH', validators = [Required(message='Required'), NumberRange(min=0, max=10, message='Must enter a number between 1 and 10')])
    PTO = TextField('PTO', validators = [Required(message='Required'), NumberRange(min=0, max=10, message='Must enter a number between 1 and 10')])
    Benefits = TextField('Benefits', validators = [Required(message='Required'), NumberRange(min=0, max=10, message='Must enter a number between 1 and 10')])
    Collaboration = TextField('Collaboration', validators = [Required(message='Required'), NumberRange(min=0, max=10, message='Must enter a number between 1 and 10')])