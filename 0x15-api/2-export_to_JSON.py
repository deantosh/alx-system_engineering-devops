#!/usr/bin/python3
"""
Script exports data in JSON format.
Requirements:
  - Records all tasks that are owned by this employee
  - Format must be: { "USER_ID": [
      {"task": "TASK_TITLE","completed": TASK_COMPLETED_STATUS,\
 "username": "USERNAME"},
      {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,\
 "username": "USERNAME"}, ... ]}
  - File name must be: USER_ID.json
"""
import json
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) == 2:
        id = sys.argv[1]
    else:
        sys.exit(1)

    # url
    url = f"https://jsonplaceholder.typicode.com/users/{id}"

    # get data from API
    employee_data = requests.get(url)
    data = employee_data.json()
    employee_todos = requests.get(f"{url}/todos")
    todos = employee_todos.json()

    # create list of employee dict
    employee_dict_list = []
    for todo in todos:
        employee_dict = {}
        employee_dict["task"] = todo["title"]
        employee_dict["completed"] = todo["completed"]
        employee_dict["username"] = data["username"]
        employee_dict_list.append(employee_dict)

    my_dict = {}
    my_dict[f"{id}"] = employee_dict_list
    json_data = json.dumps(my_dict)
    with open(f"{id}.json", "w") as file:
        file.write(json_data)
