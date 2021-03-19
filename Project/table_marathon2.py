import sqlite3
conn = sqlite3.connect(r'C:\Users\User\Desktop\Chanathivat_python\Project\Marathon.db')
c = conn.cursor()

c.execute("""CREATE TABLE marathon2 (id integer PRIMARY KEY AUTOINCREMENT,
    fname NULL,
    lname NULL,
    ids NULL,
    typerun NULL,
    timex NULL)""")

conn.commit()
conn.close()