import sqlite3

conn= sqlite3.connect("data2.db")

print("Opened the db successfully")

conn.execute("CREATE TABLE students(id INTEGER PRIMARY KEY, name TEXT, addr TEXT,city TEXT, pin TEXT)")

print("Table created")

conn.close()