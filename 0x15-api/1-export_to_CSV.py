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


# validate user input
if len(sys.argv) == 2:
    employee_id = sys.argv[1]
else:
    print("USAGE: <scriptname> <employee_id>")
    sys.exit(1)

# get data covert to JSON
user_detail = requests.get(
    f"https://jsonplaceholder.typicode.com/users/{employee_id}")
response = requests.get(
    f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")
data = response.json()

employee_data_list = []
user_data = user_detail.json()
name = user_data.get("username")
# create employee dict using the given format
for row in data:
    employee_data = dict()
    employee_data["userId"] = row["userId"]
    employee_data["name"] = name
    employee_data["completed"] = row["completed"]
    employee_data["title"] = row["title"]
    employee_data_list.append(employee_data)

fieldnames = (employee_data_list[0].keys())
with open("USER_ID.csv", "w", newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
    writer.writeheader()
    for row in employee_data_list:
        writer.writerow(row)
