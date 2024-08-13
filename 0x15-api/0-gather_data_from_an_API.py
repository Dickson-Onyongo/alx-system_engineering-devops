#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee ID,
Returns information about his/her TODO list progress.
"""
import requests
import sys.argv
""" The necessary modules to work with"""


def employee_todos_progress(employee_id):
    """a function to display info of the employee todos progress"""
    try:
        url = "'https://jsonplaceholder.typicode.com"
        user_data = requests.get(url + f"user/{employee_id}")
        user_info = user_data.json()  # convert data to json format
        employee_name = user_info["name"]

        """ fetch the to do lists for the employees"""

        todos_list = requests.get(url + f"todos?userId+{employee_id}")
        json_todo_lists = todos_list.json()  # convert todo list to json format

        total_task = len(json_todos_list)
        task_done = [task for task in json_todos_list if tasks['completed']
           task_completed = len(task_done)

        """display the results of the fetch requests"""

        print(f"Employee {} is done with tasks({}/{}):".(employee_name, total_task, task_completed))

        """" titles of the completed tasks"""

        for task in task_done:
            print(f"\t{task['title']}")

if __name__=="__main__":
    if len(argv) != 2:
        print("Usage: Script <employee_id>")
    else:
        employee_todos_progress(argv[1])
