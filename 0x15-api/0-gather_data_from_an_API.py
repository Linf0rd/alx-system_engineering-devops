#!/usr/bin/python3

"""
Retrieves and displays information about an employee's,
TODO list progress from a REST API.
"""

import requests


def get_employee_todo_progress(employee_id):
    """Fetches and processes employee TODO list progress data."""

    base_url = "https://jsonplaceholder.typicode.com/"
    employee_url = f"{base_url}users/{employee_id}"
    todos_url = f"{base_url}todos?userId={employee_id}"

    response = requests.get(employee_url)
    employee_data = response.json()
    employee_name = employee_data.get("name")

    response = requests.get(todos_url)
    todos_data = response.json()

    completed_todos = [todo for todo in todos_data if todo.get("completed")]
    number_of_done_tasks = len(completed_todos)
    total_number_of_tasks = len(todos_data)

    print(f"Employee {employee_name} is done with tasks"
          f"({number_of_done_tasks}/{total_number_of_tasks}):")

    for todo in completed_todos:
        task_title = todo.get("title")
        print("    ", task_title)


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
