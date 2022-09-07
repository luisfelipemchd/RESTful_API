#! /home/luis_machado/projects/api_flask/bin/python3

import sqlite3

connection = sqlite3.connect('project/database.db')


with open('project/schema.sql') as f:
    connection.executescript(f.read())

connection.close()