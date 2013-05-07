from flask.ext.wtf import Form, TextField, BooleanField, TextAreaField
from flask.ext.wtf import Required, Length, NumberRange, HiddenField, IntegerField, FieldList, FormField
import wtforms

class LoginForm(Form):
    openid = TextField('openid', validators = [Required()])
    remember_me = BooleanField('remember_me', default = False)

class EditForm(Form):
    nickname = TextField('nickname', validators = [Required()])
    age = TextField('age', validators = [])
    gender = TextField('gender', validators = [])
    location = TextField('location', validators = [])
    about_me = TextAreaField('about_me', validators = [Length(min = 0, max = 140)])

class AddCoForm(Form):
    name = TextField('name', validators = [Required()])
    url = TextField('url', validators = [Required()])
    location = TextField('location', validators = [Required()])
    service = TextField('service', validators = [])
    industry = TextField('industry', validators = [Required()])

class ValueRatingForm(wtforms.Form):
    value_id = HiddenField()
    value_rating = IntegerField()
    value_name = HiddenField(validators=[Required(False)])

class RateCoForm(Form):
    value_ratings = FieldList(FormField(ValueRatingForm))

