import sqlite3
conn = sqlite3.connect(r'C:\Users\User\Desktop\Chanathivat_python\Project\Marathon.db')
c = conn.cursor()

c.execute("""CREATE TABLE marathon (id integer PRIMARY KEY AUTOINCREMENT,
    fname varchar(30) NULL,
    lname varchar(30) NULL,
    ids varchar(20) NULL,
    sex varchar(10) NULL,
    age varchar(10) NULL,
    typerun varchar(30) NULL,
    email varchar(50) NULL,
    num varchar(10) NULL)""")
    
conn.commit()
conn.close()