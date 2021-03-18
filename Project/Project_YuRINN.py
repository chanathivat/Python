import os
import sqlite3

conn = sqlite3.connect(r'C:\Users\User\Desktop\Chanathivat_python\Project\Marathon.db')
c = conn.cursor()

def menu():
    global choice
    print('กรอกข้อมูล a ')
    print('เช็ตข้อมูล b ')
    print('สำหรับแอดมิน c ')
    print('ปิด exit\n')
    choice = input('เลือกรายการ ')

def add():
    fname,lname = input('ชื่อ-สกุล\t').split()
    ids = input('เลขประจำตัวประชาชน\t')
    sex = input('เพศ\t')
    age = input('อายุ\t')
    typerun = input('ประเภทการวิ่ง [full/half/mini/funrun]\t')
    email = input('อีเมล\t')
    num = input('เบอร์โทร\t')

    def add2():
        conn = sqlite3.connect(r'C:\Users\User\Desktop\Chanathivat_python\Project\Marathon.db')
        c = conn.cursor()
        sql = '''INSERT INTO marathon (fname,lname,ids,sex,age,typerun,email,num) VALUES (?,?,?,?,?,?,?,?)'''
        data = (fname,lname,ids,sex,age,typerun,email,num)
        c.execute(sql,data)
        conn.commit()
        c.close()
        print('เพิ่มข้อมูลเรียบร้อย')
    add2()

def showx():
            conn = sqlite3.connect(r'C:\Users\User\Desktop\Chanathivat_python\Project\Marathon.db')
            c = conn.cursor()
            idx = input('ตรวจสอบเลขบัตร\t')#
            idxx = (idx,)
            find_user = ('SELECT * FROM marathon WHERE ids = ?')
            c.execute(find_user,idxx,)
            resultx = c.fetchmany()
            for x in resultx :
                print ('เลขที่\t{0:<8}\nชื่อ-สกุล\t{1:<15}{2:<15}\nเลขประจำตัวประชาชน\t{3:<27}\nเพศ\t{4}\nอายุ\t{5}\nประเภทการวิ่ง\t{6}\nอีเมล\t{7}\nเบอร์โทร\t{8}\n\n'.format(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8]))
            conn.commit()
            conn.close()

def admin():
    loginx = input('\nlogin ')
    passwordx = input('pass ') 
    conn = sqlite3.connect(r'C:\Users\User\Desktop\Chanathivat_python\Project\Marathon.db')
    c = conn.cursor()
    statement = f"SELECT username from adminzz WHERE username='{loginx}' AND Password = '{passwordx}';"
    c.execute(statement)
    if not c.fetchone():
        print("Login failed")
    else:
        print("\n+++++++เข้าสู่ระบบแล้ว+++++++\n")
        def adminmenu():
            global choice2
            print('ลบข้อมูล a')
            print('เช็คข้อมูลผู้สมัคร b ')
            print('ออกจากระบบ exit ')
            choice2 = input('เลือกทำรายการ')

        def dele():
            del_id = input('เลขที่ต้องการลบ : ')
            def dele2():
                conn = sqlite3.connect(r'C:\Users\User\Desktop\Chanathivat_python\Project\Marathon.db')
                c = conn.cursor()
                c.execute('DELETE FROM marathon WHERE ids = {}'.format(del_id))
                conn.commit()
                c.close()
                print('ลบข้อมูลเรียบร้อย\n')
            dele2()

        def show():
            print('\nแสดงข้อมูลทั้งหมด a ')
            print('แสดงข้อมูลรายบุคคล b ')
            print('แสดงข้อมูลประเภท [full/half/mini/funrun]')
            showa = input('เลือกทำรายการ ')
            
            def show2():
                conn = sqlite3.connect(r'C:\Users\User\Desktop\Chanathivat_python\Project\Marathon.db')
                c = conn.cursor()
                idx = input('ตรวจสอบเลขบัตร\t')#
                idxx = (idx,)
                find_user = ('SELECT * FROM marathon WHERE ids = ?')
                c.execute(find_user,idxx,)
                resultz = c.fetchmany()
                for x in resultz :
                    print ('เลขที่\t{0:<8}\nชื่อ-สกุล\t{1:<15}{2:<15}\nเลขประจำตัวประชาชน\t{3:<27}\nเพศ\t{4}\nอายุ\t{5}\nประเภทการวิ่ง\t{6}\nอีเมล\t{7}\nเบอร์โทร\t{8}\n\n'.format(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8]))
                conn.commit()
                conn.close()
            def show3():
                conn = sqlite3.connect(r'C:\Users\User\Desktop\Chanathivat_python\Project\Marathon.db')
                c = conn.cursor()
                c.execute('''SELECT * FROM marathon''')
                result = c.fetchall()
                for x in result :
                    print ('เลขที่\t{0:<8}\nชื่อ-สกุล\t{1:<15}{2:<15}\nเลขประจำตัวประชาชน\t{3:<27}\nเพศ\t{4}\nอายุ\t{5}\nประเภทการวิ่ง\t{6}\nอีเมล\t{7}\nเบอร์โทร\t{8}\n\n'.format(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8]))
                conn.commit()
                conn.close()
            def showfull():
                conn = sqlite3.connect(r'C:\Users\User\Desktop\Chanathivat_python\Project\Marathon.db')
                c = conn.cursor()
                c.execute(' SELECT * FROM marathon WHERE typerun = "full"')
                resultfull = c.fetchall()
                for x in resultfull:
                    print ('เลขที่\t{0:<8}\nชื่อ-สกุล\t{1:<15}{2:<15}\nเลขประจำตัวประชาชน\t{3:<27}\nเพศ\t{4}\nอายุ\t{5}\nประเภทการวิ่ง\t{6}\nอีเมล\t{7}\nเบอร์โทร\t{8}\n\n'.format(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8]))
            def showhalf():
                conn = sqlite3.connect(r'C:\Users\User\Desktop\Chanathivat_python\Project\Marathon.db')
                c = conn.cursor()
                c.execute(' SELECT * FROM marathon WHERE typerun = "half"')
                resulthalf = c.fetchall()
                for x in resulthalf:
                    print ('เลขที่\t{0:<8}\nชื่อ-สกุล\t{1:<15}{2:<15}\nเลขประจำตัวประชาชน\t{3:<27}\nเพศ\t{4}\nอายุ\t{5}\nประเภทการวิ่ง\t{6}\nอีเมล\t{7}\nเบอร์โทร\t{8}\n\n'.format(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8]))
            def showmini():
                conn = sqlite3.connect(r'C:\Users\User\Desktop\Chanathivat_python\Project\Marathon.db')
                c = conn.cursor()
                c.execute(' SELECT * FROM marathon WHERE typerun = "mini"')
                resultmini = c.fetchall()
                for x in resultmini:
                    print ('เลขที่\t{0:<8}\nชื่อ-สกุล\t{1:<15}{2:<15}\nเลขประจำตัวประชาชน\t{3:<27}\nเพศ\t{4}\nอายุ\t{5}\nประเภทการวิ่ง\t{6}\nอีเมล\t{7}\nเบอร์โทร\t{8}\n\n'.format(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8]))
            def showfunrun():
                conn = sqlite3.connect(r'C:\Users\User\Desktop\Chanathivat_python\Project\Marathon.db')
                c = conn.cursor()
                c.execute(' SELECT * FROM marathon WHERE typerun = "funrun"')
                resultfunrun = c.fetchall()
                for x in resultfunrun:
                    print ('เลขที่\t{0:<8}\nชื่อ-สกุล\t{1:<15}{2:<15}\nเลขประจำตัวประชาชน\t{3:<27}\nเพศ\t{4}\nอายุ\t{5}\nประเภทการวิ่ง\t{6}\nอีเมล\t{7}\nเบอร์โทร\t{8}\n\n'.format(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8]))
            if showa == 'a':
                show3()
            elif showa == 'b':
                show2()
            elif showa == 'full':
                showfull()
            elif showa == 'half':
                showhalf()
            elif showa == 'mini':
                showmini()
            elif showa == 'funrun':
                showfunrun()

        while True:
            adminmenu()
            if  choice2 == 'a':
                dele()
            if choice2 == 'b':
                show()
            elif choice2 == 'exit':
                print('++++++++++ออกจากระบบแล้ว++++++++\n')
                break

            
while True:
    menu()
    if choice == 'a':
        add()
        os.system('cls')
    elif choice == 'b':
        showx()
    elif choice == 'c':
        admin()
    elif choice == 'exit':
        break