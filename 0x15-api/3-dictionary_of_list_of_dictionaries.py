#!/usr/bin/python3
"""
Script exports data in JSON format.
Requirements:
  - Records all tasks from all employees
  - Format must be: { "USER_ID": [{"username": "USERNAME", "task":\
 "TASK_TITLE", "completed": TASK_COMPLETED_STATUS},{"username":\
 "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS},\
 ... ], "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE",\
 "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task":\
 "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}
  - File name must be: todo_all_employees.json
"""
import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users"
    # get data from API
    user_data = requests.get(url)
    users = user_data.json()

    # create employee todo list
    employees_todos_dict = {}
    for user in users:
        id = user["id"]
        user_todo_data = requests.get(f"{url}/{id}/todos")
        todos = user_todo_data.json()
        employee_todos_list = []
        for todo in todos:
            emp_todo_dict = {}
            emp_todo_dict["username"] = user["username"]
            emp_todo_dict["task"] = todo["title"]
            emp_todo_dict["completed"] = todo["completed"]
            employee_todos_list.append(emp_todo_dict)
        # add to dict
        employees_todos_dict[f"{id}"] = employee_todos_list
    employees_todos_data = json.dumps(employees_todos_dict)

    # write into json file
    with open("todo_all_employees.json", "w") as file:
        file.write(employees_todos_data)
