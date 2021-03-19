import os
import sqlite3

conn = sqlite3.connect(r'C:\Users\User\Desktop\Chanathivat_python\Project\Marathon.db')
c = conn.cursor()

def menu():
    global choice
    print('กรอกข้อมูล [a] ')
    print('เช็ตข้อมูล [b] ')
    print('แสดงผลการวิ่ง [c]')
    print('สำหรับแอดมิน [l] ')
    print('ปิด [exit]\n')
    choice = input('เลือกรายการ ')

def add():
    fname,lname = input('ชื่อ-สกุล\t').split()
    ids = int(input('เลขประจำตัวประชาชน\t'))
    sex = str(input('เพศ\t'))
    age = int(input('อายุ\t'))
    typerun = str(input('ประเภทการวิ่ง [full/half/mini/funrun]\t'))
    email = input('อีเมล\t')
    num = str(input('เบอร์โทร\t'))

    def add2():
        conn = sqlite3.connect(r'C:\Users\User\Desktop\Chanathivat_python\Project\Marathon.db')
        c = conn.cursor()
        sql = '''INSERT INTO marathon (fname,lname,ids,sex,age,typerun,email,num) VALUES (?,?,?,?,?,?,?,?)'''
        data = (fname,lname,ids,sex,age,typerun,email,num)
        sql2 = '''INSERT INTO marathon2 (fname,lname,ids,typerun) VALUES (?,?,?,?)'''
        data2 = (fname,lname,ids,typerun)
        c.execute(sql,data)
        c.execute(sql2,data2)
        conn.commit()
        c.close()
        print('เพิ่มข้อมูลเรียบร้อย')
    add2()

def showx():
        conn = sqlite3.connect(r'C:\Users\User\Desktop\Chanathivat_python\Project\Marathon.db')
        c = conn.cursor()
        idx = int(input('\nตรวจสอบเลขบัตร\t'))#
        idxx = (idx,)
        find_user = ('SELECT * FROM marathon WHERE ids = ?')
        c.execute(find_user,idxx,)
        x = c.fetchone()   
        if  not x:
            print("\nไม่พบข้อมูล!\n")
        else: 
            print ('\nเลขที่\t{0:<8}\nชื่อ-สกุล\t{1:<15}{2:<15}\nเลขประจำตัวประชาชน\t{3:<27}\nเพศ\t{4}\nอายุ\t{5}\nประเภทการวิ่ง\t{6}\nอีเมล\t{7}\nเบอร์โทร\t{8}\n\n'.format(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8]))
            conn.commit()
            conn.close()

def showxx():
        conn = sqlite3.connect(r'C:\Users\User\Desktop\Chanathivat_python\Project\Marathon.db')
        c = conn.cursor()
        idx2 = int(input('\nตรวจสอบเลขบัตร\t'))#
        idxx2 = (idx2,)
        find_user = ('SELECT * FROM marathonn WHERE ids = ?')
        c.execute(find_user,idxx2,)
        x = c.fetchone()    
        if  not x:
            print("\nไม่พบข้อมูล!\n")
        else:
            print ('เลขที่\t{0:<8}\nชื่อ-สกุล\t{1:<15}{2:<15}\nเลขประจำตัวประชาชน\t{3:<27}\nประเภทการวิ่ง\t{4}\nเวลา\t{5}\n\n'.format(x[0],x[1],x[2],x[3],x[4],x[5]))
            conn.commit()
            conn.close()

def admin():
    loginx = input('\nLogin ')
    passwordx = input('Password ') 
    conn = sqlite3.connect(r'C:\Users\User\Desktop\Chanathivat_python\Project\Marathon.db')
    c = conn.cursor()
    statement = f"SELECT username from admin WHERE username='{loginx}' AND Password = '{passwordx}';"
    c.execute(statement)
    if not c.fetchone():
        print("\nLogin failed!")
    else:
        print("\n+++++++เข้าสู่ระบบแล้ว+++++++\n")
        def adminmenu():
            global choice2
            print('ลบข้อมูล [a]')
            print('เช็คข้อมูลผู้สมัคร [b] ')
            print('แก้ไขข้อมูล [e]')
            print('เพิ่มเวลา/แก้เวลา [et]')
            print('ออกจากระบบ [exit] ')
            choice2 = input('เลือกทำรายการ')

        def dele():
            del_id = input('\nเลขบัตรที่ต้องการลบ : ')
            def dele2():
                conn = sqlite3.connect(r'C:\Users\User\Desktop\Chanathivat_python\Project\Marathon.db')
                c = conn.cursor()
                c.execute('DELETE FROM marathon WHERE ids = {}'.format(del_id))
                conn.commit()
                c.close()
                print('ลบข้อมูลเรียบร้อย\n')
            dele2()

        def show():
            print('\nแสดงข้อมูลทั้งหมด [a] ')
            print('แสดงข้อมูลรายบุคคล [b] ')
            print('แสดงข้อมูลประเภท [full/half/mini/funrun]')
            showa = input('เลือกทำรายการ ')
            
            def show2():
                conn = sqlite3.connect(r'C:\Users\User\Desktop\Chanathivat_python\Project\Marathon.db')
                c = conn.cursor()
                idx = input('\nรวจสอบเลขบัตร\t')
                idxx = (idx,)
                find_user = ('SELECT * FROM marathon WHERE ids = ?')
                c.execute(find_user,idxx,)
                x = c.fetchone()
                print ('เลขที่\t{0:<;;8}\nชื่อ-สกุล\t{1:<15}{2:<15}\nเลขประจำตัวประชาชน\t{3:<27}\nเพศ\t{4}\nอายุ\t{5}\nประเภทการวิ่ง\t{6}\nอีเมล\t{7}\nเบอร์โทร\t{8}\n\n'.format(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8]))
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

        def edit():
            conn = sqlite3.connect(r'C:\Users\User\Desktop\Chanathivat_python\Project\Marathon.db')
            c = conn.cursor()
            iid = input('\nเลือกเลขที่ต้องการแก้ไข : ')
            fname,lname = input('ชื่อ-สกุล >>> ').split()
            ids = input('เลขบัตรประจำตัวประชาชน >>> ')
            sex = input('เพศ >>> ')
            age = input('อายุ >>> ')
            typerun = input('ประเภท >>> ')
            email = input('อีเมล >>> ')
            num = input('เบอร์โทร >>> ')
            data = (fname,lname,ids,sex,age,typerun,email,num,'{}'.format(iid))
            c.execute('''UPDATE marathon SET fname =?, lname =?, ids =?, sex =?, age =?, typerun =? ,email =? , num = ? WHERE id = ?''',data)
            conn.commit()
            c.close()
            print('แก้ไขข้อมูลเรียบร้อย\n')

        def edit2():
            conn = sqlite3.connect(r'C:\Users\User\Desktop\Chanathivat_python\Project\Marathon.db')
            c = conn.cursor()
            iid = input('\nเลือกเลขที่ต้องการแก้ไข : ')
            timex = input('เวลา >>> ')
            data = (timex,'{}'.format(iid))
            c.execute('''UPDATE marathon2 SET timex = ? WHERE id = ?''',data)
            conn.commit()
            c.close()
            print('แก้ไขข้อมูลเรียบร้อย\n')

        while True:
            adminmenu()
            if  choice2 == 'a':
                dele()
            if choice2 == 'b':
                show()
            if choice2 == 'e':
                edit()
            elif choice2 == 'et':
                edit2()
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
        showxx()
    elif choice == 'l':
        admin()
    elif choice == 'exit':
        break