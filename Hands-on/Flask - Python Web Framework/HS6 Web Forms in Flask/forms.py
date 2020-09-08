from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators

# Define QuoteForm below
class QuoteForm(FlaskForm):
  qauthor = StringField("Quote Author",
                        [validators.DataRequired(message='[This field is required.]'),
                         validators.Length(min=3, max=100,message='[Field must be between 3 and 100 characters long.]')])
  qstring = StringField("Quote",
                        [validators.DataRequired('[This field is required.]'),
                        validators.Length(min=3, max=200,message='[Field must be between 3 and 200 characters long.]')])
  submit = SubmitField("Add Quote")