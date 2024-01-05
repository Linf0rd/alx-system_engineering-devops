#!/usr/bin/python3

"""
Retrieves and displays information about an employee's,
TODO list progress from a REST API.
"""

import requests
import json
import sys


def export_to_json(employee_id, completed_todos):
    """Exports completed tasks data to a JSON file."""

    file_name = f"{employee_id}.json"
    data_to_export = {str(employee_id): completed_todos}

    with open(file_name, 'w', encoding='utf-8') as json_file:
        json.dump(data_to_export, json_file, ensure_ascii=False, indent=4)

    print(f"Data exported to {file_name}")


def get_employee_todo_progress(employee_id):
    """Fetches and processes employee TODO list progress data."""

    base_url = "https://jsonplaceholder.typicode.com/"
    employee_url = f"{base_url}users/{employee_id}"
    todos_url = f"{base_url}todos?userId={employee_id}"

    response = requests.get(employee_url)
    employee_data = response.json()
    employee_name = employee_data.get("username")

    response = requests.get(todos_url)
    todos_data = response.json()

    completed_todos = [
        {"task": todo.get("title"), "completed": todo.get("completed"),
            "username": employee_name}
        for todo in todos_data if todo.get("completed")
    ]

    number_of_done_tasks = len(completed_todos)
    total_number_of_tasks = len(todos_data)

    print(f"Employee {employee_name} is done with tasks"
          f"({number_of_done_tasks}/{total_number_of_tasks}):")

    for todo in completed_todos:
        print("    ", todo["task"])

    export_to_json(employee_id, completed_todos)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
