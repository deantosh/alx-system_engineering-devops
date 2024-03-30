#!/usr/bin/python3
"""
Script export data obtained from REST API to a CSV file
Requirements:
  - Records all tasks that are owned by this employee
  - Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
  - File name must be: USER_ID.csv
"""
import csv
import requests
import sys


if __name__ == "__main__":
    # validate input
    if len(sys.argv) == 2:
        employee_id = sys.argv[1]
    else:
        sys.exit(1)

    # query API to get data
    employee_detail = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    employee_detail = employee_detail.json()
    username = employee_detail["username"]
    employee_todos = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")
    employee_todos = employee_todos.json()
    # create the dict to write to the csv file
    employee_todo_list = []
    for todo in employee_todos:
        employee_todo = dict()
        employee_todo["userId"] = todo["userId"]
        employee_todo["title"] = todo["title"]
        employee_todo["completed"] = todo["completed"]
        employee_todo["username"] = username
        # append dict to list
        employee_todo_list.append(employee_todo)

    # define fieldname
    fieldnames = ("userId", "username", "completed", "title")
    # create and write to csv file
    with open("USER_ID.csv", "w", newline="") as csvfile:
        writer = csv.DictWriter(
            csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        writer.writeheader()
        for row in employee_todo_list:
            writer.writerow(row)
