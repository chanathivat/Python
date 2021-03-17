
import os
import sqlite3

conn = sqlite3.connect(r'C:\Users\User\Desktop\Chanathivat_python\Marathon.db')
c = conn.cursor()
# Create table
'''
c.execute("""CREATE TABLE marathon (id integer PRIMARY KEY AUTOINCREMENT,
    fname varchar(30) NOT NULL,
    lname varchar(30) NOT NULL,
    ids varchar(20) NOT NULL,
    age varchar(10) NOT NULL,
    typerun varchar(5) NOT NULL,
    email varchar(50) NOT NULL,
    num varchar(10) NOT NULL)""")
conn.commit()
conn.close()
'''

def menu():
    global choice
    print('\t\tMarathon')
    choice = input('ลงทะเบียน [1]\nตรวจสอบผลการวิ่ง [2]\nออกจาระบบ [Exit]\nเลือกทำรายการ : ')

def add():
    fname,lname = input('ชื่อ-สกุล\t').split()
    ids = input('เลขประจำตัวประชาชน\t')
    age = input('อายุ\t')
    typerun = input('ประเภทการวิ่ง\t')
    email = input('อีเมล\t')
    num = input('เบอร์โทร\t')

    def add2():
        conn = sqlite3.connect(r'C:\Users\User\Desktop\Chanathivat_python\Marathon.db')
        c = conn.cursor()
        sql = '''INSERT INTO marathon (fname,lname,ids,age,typerun,email,num) VALUES (?,?,?,?,?,?,?)'''
        data = (fname,lname,ids,age,typerun,email,num)
        c.execute(sql,data)
        conn.commit()
        c.close()
        print('เพิ่มข้อมูลเรียบร้อย')

    add2()

def show():
    idx = input('ตรวจสอบเลขบัตร\t')#

    def show2():
        conn = sqlite3.connect(r'C:\Users\User\Desktop\Chanathivat_python\Marathon.db')
        c = conn.cursor()
 #       idxx = input('ตรวจสอบเลขบัตร\t')
        idxx = (idx,)
        find_user = ('SELECT * FROM marathon WHERE ids = ?')
        c.execute(find_user,idxx,)
        result = c.fetchmany()
        for x in result :
            print ('เลขที่\t{0:<8}\nชื่อ-สกุล\t{1:<15}{2:<15}\nเลขประจำตัวประชาชน\t{3:<27}\nอายุ\t{4}\nประเภทการวิ่ง\t{5:<6}K\m\nเบอร์โทร\t{6}\nอีเมล\t{7}\n\n'.format(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7]))
        conn.commit()
        conn.close()
    show2()

while True:
    menu()
    os.system('cls')
    if choice == '1':
        add()
    if choice == '2':
        show()
    if choice == 'Exit' or choice == 'exit':
        exitt = input('ต้องการออกจากระบบหรือไม่ [Y/N]: ')
        if exitt == 'Y' or exitt == 'y':
            break
