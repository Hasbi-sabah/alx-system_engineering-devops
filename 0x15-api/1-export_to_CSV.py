#!/usr/bin/python3
""" Python script to export data in the CSV format. """

import requests
from sys import argv
import csv

url = "https://jsonplaceholder.typicode.com"
name = requests.get(url + "/users/{}".format(argv[1])).json().get("username")
todos = requests.get(url + "/user/{}/todos".format(argv[1])).json()

with open("{}.csv".format(argv[1]), mode="w") as f:
    csv_writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    for todo in todos:
        rows = [argv[1], name, todo.get("completed"), todo.get("title")]
        csv_writer.writerow(rows)
