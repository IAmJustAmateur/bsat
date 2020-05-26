import os
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bsat_cleanings.settings')

import sqlite3
from collections import namedtuple
from customers.models import Customer

con = sqlite3.connect("db.sqlite3")
cursor=con.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

cursor.execute("SELECT * FROM customers_customer") 
rows= cursor.fetchall()
 
for row in rows:
    print(row)

fields = Customer._meta.get_fields()
for field in fields:
    print(field)
