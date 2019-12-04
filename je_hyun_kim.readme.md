In this file you should list which features of the use-cases you implemented, which features you did not, which files you modified and any details the instructors should know when evaluating your code.


Use Case 1: Manage an appointment list.

Use Case Description As an air-condition technician I need to be able to maintain a list of service
appointment with my customers. The application should allow me to add new appointments, edit
existing appointments, delete appointments, and change the status of existing appointment. For
each appointment, I need to record, an appointment title, an appointment date, starting time an
duration, the location the appointment will take place (customer's address), the customer's name,
and notes.

I want to be able to see a list of appointments and quickly reorganize which appointments are
scheduled within within the day (i.e. today's appointments), which are scheduled within the week,
which are overdue, and which are completed. When selecting an appointment from the list I should
be able to view all the details of the appointment and update the appointment information. All
appointment information must be stored in the database.

I also want to have the option to filter my appointment by specifying certain criteria. In particular, I
should be able to filter my appointments in i) those that are due today, ii) those that are due during
the current week, iii) appointments completed, and iv) appointments overdue (i.e. appointment that
are not marked as completed but their due date is past the current date. Finally, I want to be able to
search my appointment list by customer name and by title. The application should allow give me the
user interface for me to specify the filtering and search criterial and provide me with an updated list of
appointment based on those criteria

service appointment
Properties:
- title
- date
- start_time
- duration
- location (address string)
- customer's name
- notes
- status (complete, incomplete)

Use Cases:
- add new appointment (DONE, app/main/forms.py app/main/routes.py app/templates/main/add_appointment.html app/main/models.py)
- edit existing appointments (DONE)
- delete appointments (DONE)
- change status of existing appointments (DONE)

- Filter which appointments are within today
- Filter within week
- Filter overdue
- Filter completed

- Filter by criteria: due today
- Filter by criteria: due current week
- Filter by criteria: appointment completed
- Filter by criteria: appointment overdue

- search appointment list by customer name
- search appointment list by title
