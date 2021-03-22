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
    try:    
        conn = sqlite3.connect(r'C:\Users\User\Desktop\Chanathivat_python\Project\Marathon.db')
        c = conn.cursor()
        ids = input('เลขประจำตัวประชาชน\t')
        if len(ids) != 13:
            c.close()
            add()       
        fname,lname = input('ชื่อ-สกุล\t').split()                    
        sex = str(input('เพศ [M/F]\t'))
        if sex == 'M' or sex == 'F' :
            pass
        else:
            c.close()
            add()                    
        age = int(input('อายุ\t'))
        typerun = str(input('ประเภทการวิ่ง [full/half/mini/funrun]\t'))
        if typerun == 'full':
            pass
        elif typerun == 'half':
            pass
        elif typerun == 'mini':
            pass
        elif typerun == 'funrun':
            pass
        else:
            c.close()
            add()
        email = input('อีเมล\t')
        num = str(input('เบอร์โทร\t'))
        if len(num) != 10:
            c.close()
            add()
        sql = '''INSERT INTO marathon (fname,lname,ids,sex,age,typerun,email,num) VALUES (?,?,?,?,?,?,?,?)'''
        data = (fname,lname,ids,sex,age,typerun,email,num)
        sql2 = '''INSERT INTO marathon2 (fname,lname,ids,typerun) VALUES (?,?,?,?)'''
        data2 = (fname,lname,ids,typerun)
        c.execute(sql,data)
        c.execute(sql2,data2)
        conn.commit()
        c.close()
        print('เพิ่มข้อมูลเรียบร้อย\n')              
    except:
        print('error')

def showx():
    try:
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
    except:
        print('ERROR!')

def showxx():
    try:
        conn = sqlite3.connect(r'C:\Users\User\Desktop\Chanathivat_python\Project\Marathon.db')
        c = conn.cursor()
        idx2 = int(input('\nตรวจสอบเลขบัตร\t'))#
        idxx2 = (idx2,)
        find_user2 = ('SELECT * FROM marathon2 WHERE ids = ?')
        c.execute(find_user2,idxx2,)
        x = c.fetchone()    
        if  not x:
            print("\nไม่พบข้อมูล!\n")
        else:
            print('\nเลขที่\t{0:<8}\nชื่อ-สกุล\t{1:<15}{2:<15}\nเลขประจำตัวประชาชน\t{3:<27}\nประเภทการวิ่ง\t{4}\nเวลา\t{5}\n\n'.format(x[0],x[1],x[2],x[3],x[4],x[5]))
            conn.commit()
            conn.close()
    except:
        print('ERROR!')

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
            try:
                del_id = input('\nเลขบัตรที่ต้องการลบ : ')
                conn = sqlite3.connect(r'C:\Users\User\Desktop\Chanathivat_python\Project\Marathon.db')
                c = conn.cursor()
                c.execute('SELECT * FROM marathon WHERE ids = {}'.format(del_id))
                b = c.fetchall()
                if not b:
                    print('ไม่พบข้อมูล!\n')
                else:
                    c.execute('DELETE FROM marathon WHERE ids = {}'.format(del_id))
                    c.execute('DELETE FROM marathon2 WHERE ids = {}'.format(del_id))
                    conn.commit()
                    c.close()
                    print('ลบข้อมูลเรียบร้อย\n')
            except:
                print('\nERROR!\n')
                

        def show():
            print('\n>แสดงข้อมูลทั้งหมด [a] ')
            print('>แสดงข้อมูลรายบุคคล [b] ')
            print('>แสดงข้อมูลประเภท [full/half/mini/funrun]')
            print('>แสดงอันดับ [s]')
            showa = input('เลือกทำรายการ ')
            
            def show2():
                conn = sqlite3.connect(r'C:\Users\User\Desktop\Chanathivat_python\Project\Marathon.db')
                c = conn.cursor()
                idx = input('\nรวจสอบเลขบัตร\t')
                idxx = (idx,)
                find_user = ('SELECT * FROM marathon WHERE ids = ?')
                c.execute(find_user,idxx,)
                x = c.fetchone()
                print ('\nเลขที่\t{0:<;;8}\nชื่อ-สกุล\t{1:<15}{2:<15}\nเลขประจำตัวประชาชน\t{3:<27}\nเพศ\t{4}\nอายุ\t{5}\nประเภทการวิ่ง\t{6}\nอีเมล\t{7}\nเบอร์โทร\t{8}\n\n'.format(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8]))
                conn.commit()
                conn.close()

            def show3():
                conn = sqlite3.connect(r'C:\Users\User\Desktop\Chanathivat_python\Project\Marathon.db')
                c = conn.cursor()
                c.execute('''SELECT * FROM marathon''')
                result = c.fetchall()
                for x in result :
                    print ('\nเลขที่\t{0:<8}\nชื่อ-สกุล\t{1:<15}{2:<15}\nเลขประจำตัวประชาชน\t{3:<27}\nเพศ\t{4}\nอายุ\t{5}\nประเภทการวิ่ง\t{6}\nอีเมล\t{7}\nเบอร์โทร\t{8}\n\n'.format(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8]))
                conn.commit()
                conn.close()

            def showfull():
                conn = sqlite3.connect(r'C:\Users\User\Desktop\Chanathivat_python\Project\Marathon.db')
                c = conn.cursor()
                c.execute(' SELECT * FROM marathon WHERE typerun = "full"')
                resultfull = c.fetchall()
                for x in resultfull:
                    print ('\nเลขที่\t{0:<8}\nชื่อ-สกุล\t{1:<15}{2:<15}\nเลขประจำตัวประชาชน\t{3:<27}\nเพศ\t{4}\nอายุ\t{5}\nประเภทการวิ่ง\t{6}\nอีเมล\t{7}\nเบอร์โทร\t{8}\n\n'.format(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8]))
                conn.commit()
                conn.close()
                
            def showhalf():
                conn = sqlite3.connect(r'C:\Users\User\Desktop\Chanathivat_python\Project\Marathon.db')
                c = conn.cursor()
                c.execute(' SELECT * FROM marathon WHERE typerun = "half"')
                resulthalf = c.fetchall()
                for x in resulthalf:
                    print ('\nเลขที่\t{0:<8}\nชื่อ-สกุล\t{1:<15}{2:<15}\nเลขประจำตัวประชาชน\t{3:<27}\nเพศ\t{4}\nอายุ\t{5}\nประเภทการวิ่ง\t{6}\nอีเมล\t{7}\nเบอร์โทร\t{8}\n\n'.format(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8]))
                conn.commit()
                conn.close()

            def showmini():
                conn = sqlite3.connect(r'C:\Users\User\Desktop\Chanathivat_python\Project\Marathon.db')
                c = conn.cursor()
                c.execute(' SELECT * FROM marathon WHERE typerun = "mini"')
                resultmini = c.fetchall()
                for x in resultmini:
                    print ('\nเลขที่\t{0:<8}\nชื่อ-สกุล\t{1:<15}{2:<15}\nเลขประจำตัวประชาชน\t{3:<27}\nเพศ\t{4}\nอายุ\t{5}\nประเภทการวิ่ง\t{6}\nอีเมล\t{7}\nเบอร์โทร\t{8}\n\n'.format(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8]))
                conn.commit()
                conn.close()

            def showfunrun():
                conn = sqlite3.connect(r'C:\Users\User\Desktop\Chanathivat_python\Project\Marathon.db')
                c = conn.cursor()
                c.execute(' SELECT * FROM marathon WHERE typerun = "funrun"')
                resultfunrun = c.fetchall()
                for x in resultfunrun:
                    print ('\nเลขที่\t{0:<8}\nชื่อ-สกุล\t{1:<15}{2:<15}\nเลขประจำตัวประชาชน\t{3:<27}\nเพศ\t{4}\nอายุ\t{5}\nประเภทการวิ่ง\t{6}\nอีเมล\t{7}\nเบอร์โทร\t{8}\n\n'.format(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8]))
                conn.commit()
                conn.close()

            def showre():
                try:
                    conn = sqlite3.connect(r'C:\Users\User\Desktop\Chanathivat_python\Project\Marathon.db')
                    c = conn.cursor()
                    ccc = input('ประเภท [full/half/mini/funrun]')
                    c.execute('SELECT * FROM  marathon2 WHERE typerun = "{}" ORDER BY timex'.format(ccc)) 
                    result = c.fetchall()
                    i=0
                    print('อันดับของ {}'.format(ccc))
                    print('-'*64)
                    print('{0:<7}{1:<15}| {2:<15}| {3:<10}| {4:<10}|'.format('RANK | ','    NAME','     ID','  TYPE','  TIME'))
                    print('-'*64)
                    for x in result:
                        i+=1
                        print(' {0:<4}| {1:<15}| {2:<15}| {3:<10}| {4:<10}|'.format(i,x[1],x[3],x[4],x[5]))
                    print('-'*64,'\n')
                    conn.commit()
                    c.close()                            
                except:
                    print('ERROR!')

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
            elif showa == 's':
                showre()

        def edit():
            try:
                conn = sqlite3.connect(r'C:\Users\User\Desktop\Chanathivat_python\Project\Marathon.db')
                c = conn.cursor()
                iid = input('\nเลือกเลขที่ต้องการแก้ไข : ')
                c.execute('SELECT * FROM marathon WHERE ids = {}'.format(iid))
                r = c.fetchone()
                if not r:
                    print('ไม่พบข้อมูล!\n')
                else:                                
                    fname,lname = input('ชื่อ-สกุล >>> ').split()
                    ids = input('เลขบัตรประจำตัวประชาชน >>> ')
                    sex = input('เพศ >>> ')
                    age = input('อายุ >>> ')
                    typerun = input('ประเภท >>> ')
                    email = input('อีเมล >>> ')
                    num = input('เบอร์โทร >>> ')
                    data = (fname,lname,ids,sex,age,typerun,email,num,'{}'.format(iid))
                    data2 = (fname,lname,ids,typerun,'{}'.format(iid))
                    c.execute('''UPDATE marathon SET fname =?, lname =?, ids =?, sex =?, age =?, typerun =? ,email =? , num = ? WHERE id = ?''',data)
                    c.execute('''UPDATE marathon2 SET fname =?, lname =?, ids =?, typerun =?  WHERE id = ?''',data2)
                    conn.commit()
                    c.close()
                    print('แก้ไขข้อมูลเรียบร้อย\n')
            except:
                print('\nERROR!\n')

        def edit2():
            try:
                conn = sqlite3.connect(r'C:\Users\User\Desktop\Chanathivat_python\Project\Marathon.db')
                c = conn.cursor()
                iid = input('\nเลือกเลขที่ต้องการแก้ไข : ')
                c.execute('SELECT * FROM marathon WHERE ids = {}'.format(iid))
                r = c.fetchone()
                if not r:
                    print('ไม่พบข้อมูล!\n')
                else:
                    timex = input('เวลา >>> ')
                    data = (timex,'{}'.format(iid))
                    c.execute('''UPDATE marathon2 SET timex = ? WHERE id = ?''',data)
                    conn.commit()
                    c.close()
                    print('แก้ไขข้อมูลเรียบร้อย\n')
            except:
                print('\nERROR!\n')

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

def ss():
    try:
        conn = sqlite3.connect(r'C:\Users\User\Desktop\Chanathivat_python\Project\Marathon.db')
        c = conn.cursor()
        ccc = input('')
        c.execute('SELECT * FROM  marathon2 WHERE typerun = "{}" ORDER BY timex'.format(ccc))
        result = c.fetchall()
        i=0
        print('อันดับของ {}'.format(ccc))
        print('-'*64)
        print('{0:<7}{1:<15}| {2:<15}| {3:<10}| {4:<10}|'.format('RANK | ','    NAME','     ID','  TYPE','  TIME'))
        print('-'*64)
        for x in result:
            i+=1
            print(' {0:<4}| {1:<15}| {2:<15}| {3:<10}| {4:<10}|'.format(i,x[1],x[3],x[4],x[5]))
        print('-'*64,'\n')
        conn.commit()        
        c.close()
    except:
        print('ERROR!')

while True:
    menu()
    if choice == 'a':
        add()
    #    os.system('cls')
    elif choice == 'b':
        showx()
    elif choice == 'c':
        showxx()
    elif choice == 'l':
        admin()
    elif choice == 'ss':
        ss()
    elif choice == 'exit':
        break