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
    val_collaboration = TextField('collaboration', validators = [])
    val_competitive_pay = TextField('competitive_pay', validators = [])
    val_empowerment = TextField('empowerment', validators = [])
    val_flex_sched = TextField('flex_sched', validators = [])
    val_advancement_opps = TextField('advancement_opps', validators = [])
    val_honesty = TextField('honesty', validators = [])
    val_innovation = TextField('innovation', validators = [])
    val_medical_benefits = TextField('medical_benefits', validators = [])
    val_mentoring = TextField('mentoring', validators = [])
    val_paid_time_off = TextField('paid_time_off', validators = [])
    val_performance_feedback = TextField('performance_feedback', validators = [])
    val_results_driven = TextField('results_driven', validators = [])
    val_retirement = TextField('retirement', validators = [])
    val_training_development = TextField('training_development', validators = [])
    val_work_from_home = TextField('work_from_home', validators = [])

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

