import sqlite3

conn = sqlite3.connect(r'C:\Users\User\Desktop\Chanathivat_python\Marathon.db')
c = conn.cursor()

def menu():
    global choice
    print('กรอกข้อมูล a ')
    print('เช็ตข้อมูล b ')
    print('สำหรับแอดมิน c ')
    print('ปิด exit')
    choice = input('เลือกรายการ \n')

def add():
    a1 = input('') 
    a2 = input('')
    a3 = input('')
    a4 = input('')
    a5 = input('')

def show():
    print('k')

def admin():
    loginx = input('login ')
    passwordx = input('pass ') 
    conn = sqlite3.connect(r'C:\Users\User\Desktop\Chanathivat_python\Marathon.db')
    c = conn.cursor()
    statement = f"SELECT username from adminzz WHERE username='{loginx}' AND Password = '{passwordx}';"
    c.execute(statement)
    if not c.fetchone():
        print("Login failed")
    else:
        print("Welcome")
        def adminmenu():
            global choice2
            print('ลบข้อมูล a')
            print('เช็คข้อมูลผู้สมัคร b ')
            print('ออกจากระบบ exit ')
            choice2 = input('เลือกทำรายการ')

        def dele():
            del_id = input('เลขที่ต้องการลบ : ')
            def dele2():
                conn = sqlite3.connect(r'C:\Users\User\Desktop\Chanathivat_python\Marathon.db')
                c = conn.cursor()
                c.execute('DELETE FROM marathon WHERE ids = {}'.format(del_id))
                conn.commit()
                c.close()
                print('ลบข้อมูลเรียบร้อย\n')
            dele2()

        def show():
            print('แสดงข้อมูลทั้งหมด a ')
            print('แสดงข้อมูลรายบุคคล b ')
            showa = input('เลือกทำรายการ ')
            
            def show2():
                conn = sqlite3.connect(r'C:\Users\User\Desktop\Chanathivat_python\Marathon.db')
                c = conn.cursor()
                idx = input('ตรวจสอบเลขบัตร\t')#
                idxx = (idx,)
                find_user = ('SELECT * FROM marathon WHERE ids = ?')
                c.execute(find_user,idxx,)
                result = c.fetchmany()
                for x in result :
                    print ('เลขที่\t{0:<8}\nชื่อ-สกุล\t{1:<15}{2:<15}\nเลขประจำตัวประชาชน\t{3:<27}\nอายุ\t{4}\nประเภทการวิ่ง\t{5:<6}K\m\nเบอร์โทร\t{6}\nอีเมล\t{7}\n\n'.format(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7]))
                conn.commit()
                conn.close()
            def show3():
                conn = sqlite3.connect(r'C:\Users\User\Desktop\Chanathivat_python\Marathon.db')
                c = conn.cursor()
                c.execute('''SELECT * FROM marathon''')
                result = c.fetchall()
                for x in result :
                    print ('เลขที่\t{0:<8}\nชื่อ-สกุล\t{1:<15}{2:<15}\nเลขประจำตัวประชาชน\t{3:<27}\nอายุ\t{4}\nประเภทการวิ่ง\t{5:<6}K\m\nเบอร์โทร\t{6}\nอีเมล\t{7}\n\n'.format(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7]))
                    conn.commit()
                    conn.close()
            if showa == 'a':
                show3()
            elif showa == 'b':
                show2()

             
        while True:
            adminmenu()
            if  choice2 == 'a':
                dele()
            if choice2 == 'b':
                show()
            elif choice2 == 'exit':
                break

            
while True:
    menu()
    if choice == 'a':
        add()
    elif choice == 'b':
        show()
    elif choice == 'c':
        admin()
    elif choice == 'exit':
        break