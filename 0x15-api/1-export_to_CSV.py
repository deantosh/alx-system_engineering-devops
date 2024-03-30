#!/usr/bin/python3
"""
Script export data obtained from REST API to a CSV file
Requirements:
  - Records all tasks that are owned by this employee
  - Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
  - File name must be: USER_ID.csv
"""
import requests
import sys


if __name__ == "__main__":
    # validate input
    if len(sys.argv) == 2:
        employee_id = sys.argv[1]
    else:
        sys.exit(1)

    # url
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"

    # query API to get data
    employee_data = requests.get(url)
    employee_todos = requests.get(f"{url}/todos")

    # convert response to json
    employee_data = employee_data.json()
    employee_todos = employee_todos.json()

    # get the user name
    username = employee_data["username"]

    # create and write to csv file
    with open(f"{employee_id}.csv", "w") as csvfile:
        for row in employee_todos:
            csvfile.write('"{}","{}","{}","{}"\n'.format(
                row["userId"], username, row["completed"], row["title"]))
