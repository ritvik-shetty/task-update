import sqlite3

conn1= sqlite3.connect("empdatabase.db")

print("Opened the db successfully")

conn1.execute("CREATE TABLE IF NOT EXISTS emp(id INTEGER PRIMARY KEY, name TEXT, addr TEXT,city TEXT, salary TEXT)")
print("Table1 created")
conn1.close()

conn2= sqlite3.connect("empdatabase.db")
conn2.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE,password TEXT")
print("Table2 created")
conn2.close()
