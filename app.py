#! /home/luis_machado/projects/api_flask/bin/python3

import sqlite3

from flask import Flask


def get_db_connection():
    conn = sqlite3.connect('project/database.db')
    conn.row_factory = sqlite3.Row

    return conn


def get_customer(customer_id):
    conn = get_db_connection()
    customer = conn.execute(f'SELECT * FROM customers WHERE customer_id = {customer_id}').fetchone()
    conn.close()
    if customer is None:
        return 'Customer Not Found!'
    return customer


app = Flask(__name__)

@app.route('/')
def index():
    conn = get_db_connection()
    customers = conn.execute('SELECT * FROM customers ORDER BY created DESC LIMIT 10').fetchall()
    conn.close()

    return {i[0]: dict(zip(['created', 'gender', 'age', 'income', 'spending_score'], i[1:])) for i in customers}


@app.route('/<int:customer_id>')
def customer(customer_id):
    customer = get_customer(customer_id)

    return {customer[0]: dict(zip(['created', 'gender', 'age', 'income', 'spending_score'], customer[1:]))}


if __name__ == '__main__':
    app.run(debug=True)