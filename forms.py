from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, TextAreaField, HiddenField, SelectField
from wtforms.validators import InputRequired, Length, Email, URL

'''def phone_number_validator(FlaskForm, field):
    if len(field.data) != 12 or field.data[3] != '.' or field.data[7] != '.':
        raise ValueError('Please enter a valid phone number')'''

class Npo_form(FlaskForm):
    name = StringField("Organization Name:", validators=[InputRequired(message="Organization name is required!"), Length(min=100, max=1000)])
    phone_number = StringField("Phone Number:", validators=[InputRequired()])
    email = StringField("Email Address:", validators=[InputRequired(message="Email address is required"), Email()])
    web_site = StringField("Organization URL:", validators=[URL(require_tld=True, message="That is not a valid URL.")])
    description = StringField("Description of Organization:", validators=[InputRequired(message="Please tell us about your organization."), Length(min=100,max=2000)])
    seeking = StringField("Description of Resources Needed:", validators=[InputRequired("Please describe what you are looking for."), Length(min=100,max=2000)])
    Contributors = SelectField("Type of Contribution Organization seeking ... ", choices=[("Donors","Select this option if you are seeking contributions of material goods."),("Volunteers","Select this option if you are seeking contributions of time."),("Donors and Volunteers","Select this option if you are seeking both contributions of material and time.")])
    submit=SubmitField("Submit")
    
'''class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    email = StringField("School Email", validators=[DataRequired()])
    submit = SubmitField()

#FORM to pass data
class QuestionForm(FlaskForm):
    question = StringField('What is your question?', validators=[DataRequired()])
    score = HiddenField('points')
    submit = SubmitField('Submit Question')

class AnswerForm(FlaskForm):
    question_id = HiddenField('id')
    answer = TextAreaField('answer', validators=[DataRequired()])
    submit = SubmitField('submit')
'''

# @app.route('/contribute', methods=['GET'])
# def show_listings():
#     if request.args.get('seeking'):
#         seeking = request.args.get('seeking')
#         listings = Npo.query.filter_by(choices=seeking).all()
#         return render_template('placehoder.html', choices=seeking)

    

