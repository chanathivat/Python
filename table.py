import sqlite3

conn = sqlite3.connect(r'C:\Users\User\Desktop\Chanathivat_python\Marathon.db')
c = conn.cursor()
'''
c.execute("""CREATE TABLE adminzz (
    Username,
    Password)""")

conn.commit()
conn.close()
'''
def addd(Username,Password):
    conn = sqlite3.connect(r'C:\Users\User\Desktop\Chanathivat_python\Marathon.db')
    c = conn.cursor()
    sql = '''INSERT INTO adminzz (Username,Password) VALUES (?,?)'''
    data=(Username,Password)
    c.execute(sql,data)
    conn.commit()
    conn.close()

addd('admin','1234')