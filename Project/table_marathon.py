import sqlite3
conn = sqlite3.connect(r'C:\Users\User\Desktop\Chanathivat_python\Project\Marathon.db')
c = conn.cursor()

c.execute("""CREATE TABLE marathon (id integer PRIMARY KEY AUTOINCREMENT,
    fname NULL,
    lname NULL,
    ids NULL,
    sex NULL,
    age NULL,
    typerun NULL,
    email NULL,
    num NULL)""")
    
conn.commit()
conn.close()