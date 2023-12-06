import sqlite3

conn= sqlite3.connect("data.db")

print("Opened the db successfully")

conn.execute("CREATE TABLE students(name TEXT, addr TEXT,city TEXT, pin TEXT)")

print("Table created")

conn.close()