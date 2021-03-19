import sqlite3
conn = sqlite3.connect(r'C:\Users\User\Desktop\Chanathivat_python\Project\Marathon.db')
c = conn.cursor()

c.execute("""CREATE TABLE marathon2 (id integer PRIMARY KEY AUTOINCREMENT,
    fname ,
    lname,
    ids,
    typerun,
    timex)""")

conn.commit()
conn.close()