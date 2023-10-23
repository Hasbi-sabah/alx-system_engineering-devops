#!/usr/bin/python3
""" Python script to export data in the JSON format. """

import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/user"
    with open("todo_all_employees.json", mode="w") as f:
        data = {}
        for i in range(1, 11):
            name = requests.get(url + "s/{}".format(i)).json().get("username")
            todos = requests.get(url + "/{}/todos".format(i)).json()
            row_list = []
            for todo in todos:
                row = {}
                row['username'] = name
                row['task'] = todo.get("title")
                row['completed'] = todo.get("completed")
                row_list.append(row)
            data[i] = row_list
        json.dump(data, f)
