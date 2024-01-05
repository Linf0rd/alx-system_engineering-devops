#!/usr/bin/python3

"""This script gets the employee tasks from the API and prints,
them to the console."""

import sys
import requests


def get_employee_tasks(employee_id):
    """Gets the employee tasks from the API.

    Args:
        employee_id: The employee ID.

    Returns:
        A list of tasks.
    """
    response = requests.get(
        "https://jsonplaceholder.typicode.com/todos",
        params={"userId": employee_id},
    )
    return response.json()


def get_employee_name(employee_id):
    """Gets the employee name from the API.

    Args:
        employee_id: The employee ID.

    Returns:
        The employee name.
    """
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users",
        params={"id": employee_id},
    )
    return response.json()[0]["name"]


def main():
    """Gets the employee tasks and prints them to the console."""
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        return

    employee_id = int(sys.argv[1])
    tasks = get_employee_tasks(employee_id)
    employee_name = get_employee_name(employee_id)

    print(f"Employee {employee_name} is done with tasks("
          f"{len(tasks)}/{len(tasks)}):")
    for task in tasks:
        if task["completed"]:
            print(f"\t{task['title']}")


if __name__ == "__main__":
    main()
