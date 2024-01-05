#!/usr/bin/python3

"""
Retrieves and displays information about an employee's TODO list,
progress from a REST API and exports the data to a CSV file.
"""

import requests
import csv


def get_employee_todo_progress_and_export_to_csv(employee_id):
    """
    Fetches, processes, and exports employee TODO list,
    progress data to CSV.
    """

    base_url = "https://jsonplaceholder.typicode.com/"
    employee_url = f"{base_url}users/{employee_id}"
    todos_url = f"{base_url}todos?userId={employee_id}"

    response = requests.get(employee_url)
    employee_data = response.json()
    employee_name = employee_data.get("username")

    response = requests.get(todos_url)
    todos_data = response.json()

    # Prepare CSV data
    csv_data = []
    for todo in todos_data:
        csv_data.append([
            f'"{employee_id}"',
            f'"{employee_name}"',
            f'"{todo.get("completed")}"',
            f'"{todo.get("title")}"'
        ])

    # Create and write to CSV file
    csv_filename = f"{employee_id}.csv"
    with open(csv_filename, "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)

        for row in csv_data:
            csvfile.write(','.join(row) + '\n')


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress_and_export_to_csv(employee_id)
