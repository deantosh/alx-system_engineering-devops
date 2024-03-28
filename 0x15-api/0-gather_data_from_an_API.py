#!/usr/bin/python3
"""
Script uses a REST API, for a given employee ID, returns information \
about his/her TODO list progress.
Requirements:
  - You must use urllib or requests module
  - The script must accept an integer as a parameter, which is the\
 employee ID
  - The script must display on the standard output the employee TODO\
 list progress in this exact format:
      => First line: Employee EMPLOYEE_NAME is done with tasks(
NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
        EMPLOYEE_NAME: name of the employee
        NUMBER_OF_DONE_TASKS: number of completed tasks
        TOTAL_NUMBER_OF_TASKS: total number of tasks, which is the sum\
 of completed and non-completed tasks
      => Second and N next lines display the title of completed tasks:\
 TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE)
"""
import requests
import sys

# validate user input
if len(sys.argv) == 2:
    employee_id = sys.argv[1]
else:
    print("USAGE <scriptname> <employee_id>")
    sys.exit(1)

# fetch data from fake API
user_detail = requests.get(
    f"https://jsonplaceholder.typicode.com/users/{employee_id}")
user_todos = requests.get(
    f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")
user_complete_todos = requests.get(
    f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos?\
completed=true")

# get the name of employee
user_data = user_detail.json()
name = user_data.get("name")

# get the number of tasks
todo_data = user_todos.json()
num_a_todos = len(todo_data)

# get number of completed tasks
completed_todos = user_complete_todos.json()
num_c_todos = len(completed_todos)

# print result
todo_string = "Employee {} is done with tasks({}/{}):".format(
    name, num_c_todos, num_a_todos)
print(todo_string)
for todo in completed_todos:
    print("\t{}".format(todo.get("title")))
