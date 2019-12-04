
#from flask import url_for
from app import db




class Task(db.Model):

    task_id = db.Column(db.Integer, primary_key=True)
    task_desc = db.Column(db.String(128), index=True)
    task_status = db.Column(db.String(128))

class Appointment(db.Model):
    task_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    date_time = db.Column(db.DateTime)
    duration = db.Column(db.Integer)
    location = db.Column(db.String)
    customer_name = db.Column(db.String)
    notes = db.Column(db.String)
    status = db.Column(db.String)
