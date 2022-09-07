#! /home/luis_machado/projects/api_flask/bin/python3

import pandas as pd
import sqlite3

conn = sqlite3.connect('project/database.db')

df = pd.read_csv('project/data/Mall_Customers.csv')

for _, r in df.iterrows():
    conn.execute('INSERT INTO customers (customer_id, gender, age, income, spending_score) VALUES (?, ?, ?, ?, ?)', (r[0], r[1], r[2], r[3], r[4]))
    conn.commit()
conn.close()