from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required


class ReasonForm(FlaskForm):
 title = StringField('Reason title',validators=[Required()])
 reason = TextAreaField('Reason for using Pomodoro',validators=[Required()])
 submit = SubmitField('Submit')
  

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')