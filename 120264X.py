
import sqlite3

conn = sqlite3.connect(r'C:\Users\User\Desktop\Chanathivat_python\Student.db')

c = conn.cursor()
# Create table
'''
c.execute("""CREATE TABLE students (id integer PRIMARY KEY AUTOINCREMENT,
    fname varchar(30) NOT NULL,
    lname varchar(30) NOT NULL,
    email varchar(100) NOT NULL,
    sex varchar(10) NOT NULL,
    age varchar(10) NOT NULL,
    year varchar(5) NOT NULL)""")
'''
def menu():
    global choice
    print('-'*5,'ระบบทะเบียนนักเรียน','-'*5)
    print('='*28,'\nเพิ่มข้อมูลนักเรียน กด [a]\nแสดงข้อมูลนักเรียน [s]\nแก้ไขข้อมูลนักเรียน [e]\nลบข้อมูลนักเรียน [d]\nออกจากระบบ [x]')
    choice = input('\nกรุณาเลือกทำรายการ :')

def show():
    conn = sqlite3.connect(r'C:\Users\User\Desktop\Chanathivat_python\Student.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM students''')
    result = c.fetchall()
    for x in result :
        print(x)
    conn.commit()
    conn.close()

def add(fname,lname,email,sex,age,year):
    try :
        conn = sqlite3.connect(r'C:\Users\User\Desktop\Chanathivat_python\Student.db')
        c = conn.cursor()
        sql = '''INSERT INTO students (fname,lname,email,sex,age,year) VALUES (?,?,?,?,?,?)'''
        data = (fname,lname,email,sex,age,year)
        c.execute(sql,data)
        conn.commit()
        c.close()

    except sqlite3.Error as e :
        print(e)
    finally :
        if conn :
            conn.close()
 
while True:
    menu()
    if choice == 's':
        show()
    elif choice == 'a':
        a,b,c,d,e,f = input('ชื่อ-สกุล-อีเมล-เพศ-อายุ-ชั้นปี : ').split()
        add(a,b,c,d,e,f)
        print('เพิ่มข้อมูลเรียบร้อยแล้ว')
    elif choice == 'x':
        yesno = input('ต้องการออกจากระบบหรือไม่ [y/n]:')
        if yesno == 'Y' or yesno == 'y':
            print('ออกจากระบบเรียบร้อยแล้ว')
            break
        elif yesno == 'N' or yesno == 'n':
            print('ได้ทำการกลับสู่ระบบแล้ว')
            continue
        else:
            print('Fail!')