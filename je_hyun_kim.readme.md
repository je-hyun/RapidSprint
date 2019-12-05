SUMMARY: All use cases implemented. Status of appointments changed in the same place where edit appointment is changed.

Use Cases:
- add new appointment (DONE, app/main/forms.py app/main/routes.py app/templates/main/add_appointment.html app/main/models.py)
- edit existing appointments (DONE, see routes.py function edit_appointment)
- delete appointments (DONE, routes.py see function delete_appointment)
- change status of existing appointments (DONE, see routes.py function edit_appointment)

- Filter by criteria: due today (DONE, see list_appointments in routes.py)
- Filter by criteria: due current week (DONE, see list_appointments in routes.py)
- Filter by criteria: appointment completed (DONE, see list_appointments in routes.py)
- Filter by criteria: appointment overdue (DONE, see list_appointments in routes.py)

- search appointment list by customer name (DONE see search_appointment/search_result in routes.py)
- search appointment list by title (DONE see search_appointment/search_result in routes.py)
