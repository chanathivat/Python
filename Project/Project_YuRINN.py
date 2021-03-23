import os
import sqlite3

conn = sqlite3.connect(r'C:\Users\User\Desktop\Chanathivat_python\Project\Marathon.db')
c = conn.cursor()

def menu():
    global choice
    print('-'*39)
    print('| {0:<25}|{1:<10}|'.format(' Register','    a '))
    print('| {0:<25}|{1:<10}|'.format(' Check Information','    b '))
    print('| {0:<25}|{1:<10}|'.format(' Check running result','    c '))
    print('| {0:<25}|{1:<10}|'.format(' Admin only','    l '))
    print('| {0:<25}|{1:<10}|'.format(' Close the program','   exit '))
    print('-'*39)
    choice = input('- Select > ')

def add():
    try:    
        conn = sqlite3.connect(r'C:\Users\User\Desktop\Chanathivat_python\Project\Marathon.db')
        c = conn.cursor()
        ids = str(input('ID card number\t'))
        if len(ids) != 13:
            c.close()
            add()         
        c.execute('SELECT * FROM marathon WHERE ids = "{}"'.format(ids))
        b = c.fetchone()    
        if not b:
            fname,lname = input('Name - Surname\t').split()                    
            sex = str(input('Gender [M/F]\t'))
            if sex == 'M' or sex == 'F' :
                pass
            else:
                c.close()
                add()                    
            age = int(input('Age\t'))
            typerun = str(input('Running Type [full/half/mini/funrun]\t'))
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
            email = input('Email\t')
            num = str(input('Phone number\t'))
            if len(num) != 10:
                c.close()
                add()
            sql = '''INSERT INTO marathon (fname,lname,ids,sex,age,typerun,email,num) VALUES (?,?,?,?,?,?,?,?)'''
            data = (fname,lname,ids,sex,age,typerun,email,num)
            c.execute(sql,data)
            conn.commit()
            c.close()
            print('Added successfully.\n')   
        else:
            c.close()
            print('This number already exists!!\n')
            add()           
    except:
        print('error')

def showx():
    try:
        conn = sqlite3.connect(r'C:\Users\User\Desktop\Chanathivat_python\Project\Marathon.db')
        c = conn.cursor()
        idx = str(input('\nCheck your ID card number\t'))#
        idxx = (idx,)
        find_user = ('SELECT * FROM marathon WHERE ids = ?')
        c.execute(find_user,idxx,)
        x = c.fetchone()   
        if  not x:
            print("\nNo data found!\n")
            c.close()
        else: 
            print ('\nNo\t{0:<8}\nName - Surname\t{1:<15}{2:<15}\nID card number\t{3:<27}\nGender\t{4}\nAge\t{5}\nRunning Type\t{6}\nEmail\t{7}\nPhone number\t{8}\n\n'.format(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8]))
            conn.commit()
            c.close()
    except:
        print('ERROR!')

def showxx():
    try:
        conn = sqlite3.connect(r'C:\Users\User\Desktop\Chanathivat_python\Project\Marathon.db')
        c = conn.cursor()
        idx2 = str(input('\nCheck your ID card number\t'))#
        idxx2 = (idx2,)
        find_user2 = ('SELECT * FROM marathon WHERE ids = ?')
        c.execute(find_user2,idxx2,)
        x = c.fetchone()    
        if  not x:
            print("\nNo data found!\n")
        else:
            print('\nNo\t{0:<8}\nName - Surname\t{1:<15}{2:<15}\nID card number\t{3:<27}\nRunning Type\t{4}\nTime\t{5}\n\n'.format(x[0],x[1],x[2],x[3],x[4],x[5]))
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
        print("\n--------------- Already logged in ---------------\n")
        def adminmenu():
            global choice2
            print('-'*49)
            print('| {0:<35}|{1:<10}|'.format(' Delete data','    a '))
            print('| {0:<35}|{1:<10}|'.format(' Check applicant information','    b '))
            print('| {0:<35}|{1:<10}|'.format(' Edit information','    e '))
            print('| {0:<35}|{1:<10}|'.format(' Edit time / Add time','    ea '))
            print('| {0:<35}|{1:<10}|'.format(' Log out','   exit '))
            print('-'*49)
            choice2 = input('- Select > ')

        def dele():
            try:
                del_id = input('\nInsert ID card to be deleted : ')
                conn = sqlite3.connect(r'C:\Users\User\Desktop\Chanathivat_python\Project\Marathon.db')
                c = conn.cursor()
                c.execute('SELECT * FROM marathon WHERE ids = "{}"'.format(del_id))
                b = c.fetchone()
                if not b:
                    print('No data found!\n')
                else:
                    c.execute('DELETE FROM marathon WHERE ids = "{}"'.format(del_id))
                    c.execute('DELETE FROM marathon2 WHERE ids = "{}"'.format(del_id))
                    conn.commit()
                    c.close()
                    print('The data has been deleted.\n')
            except:
                print('\nERROR!\n')
                

        def show():
            print('-'*64)
            print('| {0:<35}|{1:<25}|'.format('> Show all information','           a '))
            print('| {0:<35}|{1:<25}|'.format('> Show individual information','           b '))
            print('| {0:<35}|{1:<25}|'.format('> Show running type information','  full/half/mini/funrun'))
            print('| {0:<35}|{1:<25}|'.format('> Show rank','           s '))
            print('| {0:<35}|{1:<25}|'.format('> Back','          back '))
            print('-'*64)
            showa = input('- Select > ')
            
            def show2():
                conn = sqlite3.connect(r'C:\Users\User\Desktop\Chanathivat_python\Project\Marathon.db')
                c = conn.cursor()
                idx = input('\nCheck your ID card number\t')
                idxx = (idx,)
                find_user = ('SELECT * FROM marathon WHERE ids = ?')
                c.execute(find_user,idxx,)
                x = c.fetchone()
                print ('\nNo\t{0:<8}\nName - Surname\t{1:<15}{2:<15}\nID card number\t{3:<27}\nGender\t{4}\nAge\t{5}\nRunning Type\t{6}\nEmail\t{7}\nPhone number\t{8}\n\n'.format(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8]))
                conn.commit()
                conn.close()

            def show3():
                conn = sqlite3.connect(r'C:\Users\User\Desktop\Chanathivat_python\Project\Marathon.db')
                c = conn.cursor()
                c.execute('''SELECT * FROM marathon''')
                result = c.fetchall()
                for x in result :
                    print ('\nNo\t{0:<8}\nName - Surname\t{1:<15}{2:<15}\nID card number\t{3:<27}\nGender\t{4}\nAge\t{5}\nRunning Type\t{6}\nEmail\t{7}\nPhone number\t{8}\n\n'.format(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8]))
                conn.commit()
                conn.close()

            def showfull():
                conn = sqlite3.connect(r'C:\Users\User\Desktop\Chanathivat_python\Project\Marathon.db')
                c = conn.cursor()
                c.execute(' SELECT * FROM marathon WHERE typerun = "full"')
                resultfull = c.fetchall()
                for x in resultfull:
                    print ('\nNo\t{0:<8}\nName - Surname\t{1:<15}{2:<15}\nID card number\t{3:<27}\nGender\t{4}\nAge\t{5}\nRunning Type\t{6}\nEmail\t{7}\nPhone number\t{8}\n\n'.format(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8]))
                conn.commit()
                conn.close()
                
            def showhalf():
                conn = sqlite3.connect(r'C:\Users\User\Desktop\Chanathivat_python\Project\Marathon.db')
                c = conn.cursor()
                c.execute(' SELECT * FROM marathon WHERE typerun = "half"')
                resulthalf = c.fetchall()
                for x in resulthalf:
                    print ('\nNo\t{0:<8}\nName - Surname\t{1:<15}{2:<15}\nID card number\t{3:<27}\nGender\t{4}\nAge\t{5}\nRunning Type\t{6}\nEmail\t{7}\nPhone number\t{8}\n\n'.format(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8]))
                conn.commit()
                conn.close()

            def showmini():
                conn = sqlite3.connect(r'C:\Users\User\Desktop\Chanathivat_python\Project\Marathon.db')
                c = conn.cursor()
                c.execute(' SELECT * FROM marathon WHERE typerun = "mini"')
                resultmini = c.fetchall()
                for x in resultmini:
                    print ('\nNo\t{0:<8}\nName - Surname\t{1:<15}{2:<15}\nID card number\t{3:<27}\nGender\t{4}\nAge\t{5}\nRunning Type\t{6}\nEmail\t{7}\nPhone number\t{8}\n\n'.format(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8]))
                conn.commit()
                conn.close()

            def showfunrun():
                conn = sqlite3.connect(r'C:\Users\User\Desktop\Chanathivat_python\Project\Marathon.db')
                c = conn.cursor()
                c.execute(' SELECT * FROM marathon WHERE typerun = "funrun"')
                resultfunrun = c.fetchall()
                for x in resultfunrun:
                    print ('\nNo\t{0:<8}\nName - Surname\t{1:<15}{2:<15}\nID card number\t{3:<27}\nGender\t{4}\nAge\t{5}\nRunning Type\t{6}\nEmail\t{7}\nPhone number\t{8}\n\n'.format(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8]))
                conn.commit()
                conn.close()

            def showre():
                try:
                    conn = sqlite3.connect(r'C:\Users\User\Desktop\Chanathivat_python\Project\Marathon.db')
                    c = conn.cursor()
                    ccc = input('Type [full/half/mini/funrun]')
                    c.execute('SELECT * FROM  marathon WHERE typerun = "{}" ORDER BY timex'.format(ccc)) 
                    result = c.fetchall()
                    i=0
                    print('Rank {}'.format(ccc))
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
            if showa == 'back':
                adminmenu()


        def edit():
            try:
                conn = sqlite3.connect(r'C:\Users\User\Desktop\Chanathivat_python\Project\Marathon.db')
                c = conn.cursor()
                iid = input('\nเลือกเลขบัตรที่ต้องการแก้ไข : ')
                c.execute('SELECT * FROM marathon WHERE ids = "{}"'.format(iid))
                r = c.fetchone()
                if not r:
                    print('No data found!\n')
                else:                                
                    fname,lname = input('Name - Surname >>> ').split()
                    ids = input('ID card number >>> ')
                    sex = input('Gender >>> ')
                    age = input('Age >>> ')
                    typerun = input('Type >>> ')
                    email = input('Email >>> ')
                    num = input('Phone number >>> ')
                    data = (fname,lname,ids,sex,age,typerun,email,num,'{}'.format(iid))
                    c.execute('''UPDATE marathon SET fname =?, lname =?, ids =?, sex =?, age =?, typerun =? ,email =? , num = ? WHERE ids = ?''',data)
                    conn.commit()
                    c.close()
                    print('แก้ไขข้อมูลเรียบร้อย\n')
            except:
                print('\nERROR!\n')

        def edit2():
            try:
                conn = sqlite3.connect(r'C:\Users\User\Desktop\Chanathivat_python\Project\Marathon.db')
                c = conn.cursor()
                iid = input('\nเลือกเลขบัตรที่ต้องการแก้ไข : ')
                c.execute('SELECT * FROM marathon WHERE ids = "{}"'.format(iid))
                r = c.fetchone()
                if not r:
                    print('No data found!\n')
                else:
                    timex = input('Time >>> ')
                    data = (timex,'{}'.format(iid))
                    c.execute('''UPDATE marathon SET timex = ? WHERE ids = ?''',data)
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
            elif choice2 == 'ea':
                edit2()
            elif choice2 == 'exit':
                print('\n-------------- Logged out -------------\n')
                break

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
        os.system('cls')
        admin()
    elif choice == 'ss':
        ss()
    elif choice == 'exit':
        break