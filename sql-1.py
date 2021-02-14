
import sqlite3

conn = sqlite3.connect('Student.db')

c = conn.cursor()
# Create table

c.execute("""CREATE TABLE students (id integer PRIMARY KEY AUTOINCREMENT,
    fname varchar(30) NOT NULL,
    lname varchar(30) NOT NULL,
    email varchar(100) NOT NULL,
    sex varchar(10) NOT NULL,
    age varchar(10) NOT NULL,
    year varchar(5) NOT NULL)""")
    
conn.commit()
conn.close()