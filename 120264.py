import sqlite3
#def inserTousers (fname,lname,email):
#    try:
conn = sqlite3.connect(r'C:\Users\User\Desktop\Chanathivat_python\example.db')
c = conn.cursor()
try :
    c.execute('SELECT * FROM users ORDER BY id ')                                               #เรียงมากไปน้อยเติม DESC ต่อ id
#    data = ('C','C','C'),('D','D','D'),('E','E','E')                                           #เพิ่มทีละหลาย
#    c.executemany('INSERT INTO users (fname,lname,email) VALUES (?,?,?)',data)                 #เพิ่มทีละหลาย
#        sql = ''' INSERT INTO users (fname,lname,email) VALUES (?,?,?)'''                      #การสร้าง Function สำหรับเพิ่มข้อมูลในตาราง
#        data = (fname,lname,email)                                                             #การสร้าง Function สำหรับเพิ่มข้อมูลในตาราง
#        c.execute(sql,data)                                                                    #การสร้าง Function สำหรับเพิ่มข้อมูลในตาราง
    conn.commit()
    result = c.fetchall()
    for x in result:
        print(x)
    c.close()
except sqlite3.Error as e:
    print('Failed to insert : ',e)
finally :
    if conn :
        conn.close()
#inserTousers('Chanathivat','Panadram','Chanathivat@gmail.com')                                  #การสร้าง Function สำหรับเพิ่มข้อมูลในตาราง
#inserTousers('Yu','YuRINN','yurinn@panadram.com')                                               #การสร้าง Function สำหรับเพิ่มข้อมูลในตาราง
#c.execute('''SELECT * FROM users''')
#c.execute('''SELECT fname,lname FROM users''')
#name = ('Yu',)
#c.execute('SELECT * FROM users WHERE fname = ?',name)                                            #ผล WHERE
#result = c.fetchone()                                                                            #ผล WHERE
#print(result)
#result = c.fetchall()                                                                            #ผล
#for x in result :                                                                                #
#    print(x)                                                                                     #
#c.execute('''CREATE TABLE users (id integer PRIMARY KEY AUTOINCREMENT,
#    fname varchar(30) NOT NULL,
#    lname varchar(30) NOT NULL,
#    email varchar(100) NOT NULL)''')                                                             #สร้างตาราง
#c.execute('''INSERT INTO users (id,fname,lname,email) VALUES (NULL,'A','A','A')''')              #เพิ่มข้อมูล
#c.execute('''INSERT INTO users VALUES (NULL,'B','B','B')''')                                     #เพิ่มข้อมูล
#conn.commit()
#conn.close()