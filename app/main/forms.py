
# import flask_wtf
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField, IntegerField, RadioField
from wtforms.validators import ValidationError, DataRequired, Length
from wtforms.fields.html5 import DateField, TimeField
import datetime


class SearchForm(FlaskForm):
    searchbox = StringField('Search', validators=[DataRequired()])
    search_type = RadioField('Search by', choices=[('name','Customer Name'),('title','Appointment Title')], validators=[DataRequired()])
    submit = SubmitField('submit')

class TaskForm(FlaskForm):
    task_desc = StringField('task_desc', validators=[DataRequired()])
    task_status_completed = SelectField('Status', choices=[('todo','Todo'),('doing','Doing'),('done','Done')])
    submit = SubmitField('submit')

class AppointmentForm(FlaskForm):
    title = StringField('Title',validators=[DataRequired()], default="My Appointment Title")
    start_date = DateField('Start Date', validators=[DataRequired()], default=datetime.datetime.now().date())
    start_time = TimeField('Start Time', validators=[DataRequired()], default=datetime.datetime.now().time())
    duration = IntegerField('Duration (In minutes)', validators=[DataRequired()], default=60)
    location = StringField('Location Address',validators=[DataRequired()], default="8000 Utopia Parkway")
    customer_name = StringField('Customer Name',validators=[DataRequired()], default="Je Hyun Kim")
    notes = StringField('Notes',validators=[DataRequired()], default="Remember to bring folder!")
    status = StringField('Status',validators=[DataRequired()], default="incomplete")
    submit = SubmitField('Submit')
