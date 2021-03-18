import sqlite3
conn = sqlite3.connect(r'C:\Users\User\Desktop\Chanathivat_python\Project\Marathon.db')
c = conn.cursor()

c.execute("""CREATE TABLE marathon (id integer PRIMARY KEY AUTOINCREMENT,
    fname varchar(30) NOT NULL,
    lname varchar(30) NOT NULL,
    ids varchar(20) NOT NULL,
    sex varchar(10) NOT NULL,
    age varchar(10) NOT NULL,
    typerun varchar(30) NOT NULL,
    email varchar(50) NOT NULL,
    num varchar(10) NOT NULL)""")
conn.commit()
conn.close()