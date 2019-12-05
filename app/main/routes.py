from flask import render_template,  redirect, url_for, flash
from app.main import bp
from app import db
from app.main.forms import TaskForm, AppointmentForm, SearchForm
from app.models import Task, Appointment
import datetime
from sqlalchemy import func

@bp.route('/list_appointments/')
@bp.route('/list_appointments/<string:filter>', methods=['GET','POST'])
def list_appointments(filter="None"):
    '''
    - Filter which appointments are within today
    - Filter within week
    - Filter overdue
    - Filter completed
    '''
    appointments = Appointment.query.order_by(Appointment.date_time)
    current_date = datetime.datetime.now().date()
    datetime_now = datetime.datetime.now()

    start_of_day = datetime.time(0,0,0)
    end_of_day = datetime.time(23,59,59)

    start_of_week_day = datetime.datetime.today() - datetime.timedelta(days=datetime.datetime.today().isoweekday() % 7)
    end_of_week_day = start_of_week_day + datetime.timedelta(days=7)

    if filter == "today":
        appointments = appointments.filter(Appointment.date_time >= datetime.datetime.combine(current_date,start_of_day), Appointment.date_time <= datetime.datetime.combine(current_date,end_of_day))
    elif filter == "this_week":
        appointments = appointments.filter(Appointment.date_time >= datetime.datetime.combine(start_of_week_day,start_of_day), Appointment.date_time <= datetime.datetime.combine(end_of_week_day,end_of_day))
    elif filter == "overdue":
        appointments = appointments.filter(Appointment.date_time <= current_date)
        appointments = appointments.filter(func.lower(Appointment.status) != "complete")
    elif filter == "completed":
        appointments = appointments.filter(func.lower(Appointment.status) == "complete")

    appointments = appointments.all()
    return render_template("main/list_appointments.html", appointments=appointments, filter=filter)


# Main route of the applicaitons.
@bp.route('/', methods=['GET','POST'])
def index():
    return render_template("main/index.html")


#
#  Route for viewing and adding new tasks.
@bp.route('/todolist', methods=['GET','POST'])
def todolist():
    form = TaskForm()

    if form.validate_on_submit():
        # Get the data from the form, and add it to the database.
        new_task = Task()
        new_task.task_desc =  form.task_desc.data
        new_task.task_status = form.task_status_completed.data

        db.session.add(new_task)
        db.session.commit()

        # Redirect to this handler - but without form submitted - gets a clear form.
        return redirect(url_for('main.todolist'))

    todo_list = db.session.query(Task).all()

    return render_template("main/todolist.html",todo_list = todo_list,form= form)


#
# Route for removing a task
@bp.route('/todolist/remove/<int:task_id>', methods=['GET','POST'])
def remove_task(task_id):

    # Query database, remove items
    Task.query.filter(Task.task_id == task_id).delete()
    db.session.commit()
    return redirect(url_for('main.todolist'))


#
# Route for editing a task

@bp.route('/todolist/edit/<int:task_id>', methods=['GET','POST'])
def edit_task(task_id):
    form = TaskForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        # Get the data from the form, and add it to the database.

        current_task = Task.query.filter_by(task_id=task_id).first_or_404()
        current_task.task_desc =  form.task_desc.data
        current_task.task_status = form.task_status_completed.data

        db.session.add(current_task)
        db.session.commit()
        # After editing, redirect to the view page.
        return redirect(url_for('main.todolist'))

    # get task for the database.
    current_task = Task.query.filter_by(task_id=task_id).first_or_404()

    # update the form model in order to populate the html form.
    form.task_desc.data = current_task.task_desc
    form.task_status_completed.data = current_task.task_status

    return render_template("main/todolist_edit_view.html",form=form, task_id = task_id)

@bp.route('/add_appointment', methods=['GET','POST'])
def add_appointment():
    form = AppointmentForm()
    if form.validate_on_submit():
        new_appointment = Appointment()
        new_appointment.title=form.title.data
        new_appointment.date_time = datetime.datetime.combine(form.start_date.data,form.start_time.data)
        new_appointment.duration=form.duration.data
        new_appointment.location=form.location.data
        new_appointment.customer_name=form.customer_name.data
        new_appointment.notes=form.notes.data
        new_appointment.status=form.status.data

        db.session.add(new_appointment)
        db.session.commit()
        flash("Added the appointment")
        return redirect(url_for('main.add_appointment'))
    return render_template("main/add_appointment.html",form=form)

@bp.route('/single_appointment/<int:id>', methods=['GET','POST'])
def single_appointment(id):
    appointment = Appointment.query.get(id)
    return render_template("main/single_appointment.html", appointment=appointment)

@bp.route('/delete_appointment/<int:id>', methods=['GET','POST'])
def delete_appointment(id):
    db.session.delete(Appointment.query.get(id))
    db.session.commit()
    flash("Appointment with id " + str(id) + " deleted.")
    return redirect(url_for('main.list_appointments'))


@bp.route('/edit_appointment/<int:id>', methods=['GET','POST'])
def edit_appointment(id):
    form = AppointmentForm()
    appointment = Appointment.query.get(id)
    if form.validate_on_submit():
        appointment.title=form.title.data
        appointment.date_time = datetime.datetime.combine(form.start_date.data,form.start_time.data)
        appointment.duration=form.duration.data
        appointment.location=form.location.data
        appointment.customer_name=form.customer_name.data
        appointment.notes=form.notes.data
        appointment.status=form.status.data

        db.session.add(appointment)
        db.session.commit()
        flash("Edited the appointment!")
        return redirect(url_for('main.single_appointment', id=id))
    return render_template("main/edit_appointment.html",form=form, appointment=appointment)

@bp.route('/search_appointment/', methods=['GET','POST'])
def search_appointment():
    form = SearchForm()
    if form.validate_on_submit():
        return redirect(url_for('main.search_result', search_type=form.search_type.data,q=form.searchbox.data))
    return render_template("main/search.html",form=form)

@bp.route('/search_result/<string:search_type>/<string:q>')
def search_result(search_type,q="None"):
    if search_type == "name":
        appointments = Appointment.query.filter(Appointment.customer_name.ilike("%" +q+ "%")).order_by(Appointment.date_time)
    elif search_type == "title":
        appointments = Appointment.query.filter(Appointment.title.ilike("%" +q+ "%")).order_by(Appointment.date_time)

    appointments = appointments.all()
    return render_template("main/list_appointments.html", appointments=appointments, filter="hide")
