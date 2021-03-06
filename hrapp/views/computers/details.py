import sqlite3

from django.shortcuts import render, reverse, redirect
from hrapp.models import Computer, model_factory
from .. connection import Connection
from django.contrib.auth.decorators import login_required

#TODO: get individual computer details
def get_computer(computer_id):
    with sqlite3.connect(Connection.db_path) as conn:
 
       conn.row_factory = model_factory(Computer)
       db_cursor = conn.cursor()

       db_cursor.execute("""
            SELECT 
                c.id, 
                c.purchase_date, 
                c.decommission_date, 
                c.manufacturer, 
                c.model
            FROM hrapp_computer c
            WHERE c.id = ?;
        """, (computer_id,))

    computer = db_cursor.fetchone()
        # print(computer.manufacturer, computer.model)

    return computer

def delete_computer(computer_id):
    with sqlite3.connect(Connection.db_path) as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
            DELETE FROM hrapp_computer
            WHERE id NOT IN (
                SELECT c.id from hrapp_employeecomputer c
            )
            AND id = ?
        """, (computer_id,))

#TODO: setup and render detail template
@login_required
def computer_details(request, computer_id):
    if request.method == 'GET':
        computer = get_computer(computer_id)
        template = 'computers/detail.html'
        context = {
            'computer': computer
        }
        return render(request, template, context)
    
    elif request.method == 'POST':
        form_data = request.POST

        if (
            "actual_method" in form_data and form_data["actual_method"] == "DELETE"
        ):
            delete_computer(computer_id)

            return redirect(reverse('hrapp:computer_list'))


