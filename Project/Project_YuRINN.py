from abc import ABCMeta
import os
import sqlite3

conn = sqlite3.connect(r'C:\Users\User\Desktop\Chanathivat_python\Project\Marathon.db')
c = conn.cursor()

def menu():
    global choice
    print('-'*39)
    print('| {0:<25}|{1:<10}|'.format(' Register','    a '))
    print('| {0:<25}|{1:<10}|'.format(' Edit','    e '))
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
        ids = str(input('ID card number\t')) #asd 123
        idss = int(ids)
        if type(idss) != int:
            c.close()
            add()
        if len(ids) != 13:
            print('Please enter the ID card number of 13 digits.')
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
            if type(age) != int:
                c.close()
                add()
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
        print('Something is wrong.')
        add()

def editx():
    try:
        conn = sqlite3.connect(r'C:\Users\User\Desktop\Chanathivat_python\Project\Marathon.db')
        c = conn.cursor()
        iid = input('\nInsert ID card to be edited : ')
        c.execute('SELECT * FROM marathon WHERE ids = "{}"'.format(iid))
        r = c.fetchone()
        if not r:
            print('No data found!\n')
        else:  
            print ('\nNo\t{0:<8}\nName - Surname\t{1:<15}{2:<15}\nID card number\t{3:<27}\nGender\t{4}\nAge\t{5}\nRunning Type\t{6}\nEmail\t{7}\nPhone number\t{8}\n\n'.format(r[0],r[1],r[2],r[3],r[4],r[5],r[6],r[7],r[8]))      
            ee1 = input('edit Name - Surname y/n ')
            if ee1 == 'y':
                fname,lname = input('Name - Surname >>> ').split()
                datan = (fname,lname,'{}'.format(iid))
                c.execute('''UPDATE marathon SET fname =?, lname =? WHERE ids =? ''',datan)
            elif ee1 == 'n' :
                pass
            ee2 = input('edit Gender y/n ')
            if ee2 == 'y':
                sex = input('Gender >>> ')
                datas = (sex,'{}'.format(iid))
                c.execute('''UPDATE marathon SET sex =? WHERE ids =? ''',datas)
            elif ee2 == 'n' :
                pass 
            ee3 = input('edit Age y/n ')
            if ee3 == 'y':      
                age = int(input('Age >>> '))
                if type(age) == int:
                    dataa = (age,'{}'.format(iid))
                    c.execute('''UPDATE marathon SET age =? WHERE ids =? ''',dataa)                    
                elif type(age) != int:
                    c.close()
                    editx()
            elif ee3 == 'n' :
                pass
            ee4 = input('edit Type y/n ')
            if ee4 =='y':
                typerun = input('Type >>> ')
                if typerun == 'full':
                    datat = (typerun,'{}'.format(iid))
                    c.execute('''UPDATE marathon SET typerun =? WHERE ids =? ''',datat)
                elif typerun == 'half':
                    datat = (typerun,'{}'.format(iid))
                    c.execute('''UPDATE marathon SET typerun =? WHERE ids =? ''',datat)
                elif typerun == 'mini':
                    datat = (typerun,'{}'.format(iid))
                    c.execute('''UPDATE marathon SET typerun =? WHERE ids =? ''',datat)
                elif typerun == 'funrun':
                    datat = (typerun,'{}'.format(iid))
                    c.execute('''UPDATE marathon SET typerun =? WHERE ids =? ''',datat)
                else:
                    c.close()
                    print('Something is wrong.')
                    editx()
            elif ee4 == 'n' :
                pass
            ee5 = input('edit Email y/n ')
            if ee5 == 'y':
                email = input('Email >>> ')
                datae = (email,'{}'.format(iid))
                c.execute('''UPDATE marathon SET email =? WHERE ids =? ''',datae)
            elif ee5 == 'n' :
                pass
            ee6 = input('edit Phone number y/n ')
            if ee6 == 'y':
                num = input('Phone number >>> ')
                if len(num) == 10:
                    datann = (num,'{}'.format(iid))
                    c.execute('''UPDATE marathon SET num =? WHERE ids =? ''',datann)

            elif ee6 == 'n' :
                pass
        conn.commit()
        c.close()

        conn = sqlite3.connect(r'C:\Users\User\Desktop\Chanathivat_python\Project\Marathon.db')
        c = conn.cursor()
        c.execute('SELECT * FROM marathon WHERE ids = "{}"'.format(iid))
        b = c.fetchone()
        print ('\nNo\t{0:<8}\nName - Surname\t{1:<15}{2:<15}\nID card number\t{3:<27}\nGender\t{4}\nAge\t{5}\nRunning Type\t{6}\nEmail\t{7}\nPhone number\t{8}\n\n'.format(b[0],b[1],b[2],b[3],b[4],b[5],b[6],b[7],b[8]))      
        print('The information has been edited.\n')   
        c.close()  
    except:
        print('\nERROR!\n')

def showx():
    try:
        conn = sqlite3.connect(r'C:\Users\User\Desktop\Chanathivat_python\Project\Marathon.db')
        c = conn.cursor()
        idx = str(input('\nCheck ID card number\t'))#
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
        idx2 = str(input('\nCheck ID card number\t'))#
        idxx2 = (idx2,)
        find_user2 = ('SELECT * FROM marathon WHERE ids = ?')
        c.execute(find_user2,idxx2,)
        x = c.fetchone()    
        if  not x:
            print("\nNo data found!\n")
        else:
            print('\nNo\t{0:<8}\nName - Surname\t{1:<15}{2:<15}\nID card number\t{3:<27}\nRunning Type\t{4}\nTime\t{5}\n\n'.format(x[0],x[1],x[2],x[3],x[6],x[9]))
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
            print('| {0:<35}|{1:<25}|'.format('> Show running result','           s '))
            print('| {0:<35}|{1:<25}|'.format('> Back','          back '))
            print('-'*64)
            showa = input('- Select > ')
            
            def show2():
                try:
                    conn = sqlite3.connect(r'C:\Users\User\Desktop\Chanathivat_python\Project\Marathon.db')
                    c = conn.cursor()
                    idx2 = str(input('\nCheck ID card number\t'))#
                    idxx2 = (idx2,)
                    find_user2 = ('SELECT * FROM marathon WHERE ids = ?')
                    c.execute(find_user2,idxx2,)
                    x = c.fetchone()    
                    if  not x:
                        print("\nNo data found!\n")
                    else:
                        print('\nNo\t{0:<8}\nName - Surname\t{1:<15}{2:<15}\nID card number\t{3:<27}\nGender\t{4}\nAge\t{5}\nRunning Type\t{6}\nEmail\t{7}\nPhone number\t{8}\n\n'.format(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8]))
                        conn.commit()
                        conn.close()
                except:
                    print('ERROR!')
                    add()

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



            def showreme():
                print('-'*64)
                print('| {0:<35}|{1:<25}|'.format('> Show all running result','           a'))
                print('| {0:<35}|{1:<25}|'.format('> Show personal running results','           b'))
                print('| {0:<35}|{1:<25}|'.format('> Show type running results','           c'))
                print('| {0:<35}|{1:<25}|'.format('> Back','          back'))
                print('-'*64)
                showa2 = input('- Select > ')
                def showre():
                    try:
                        conn = sqlite3.connect(r'C:\Users\User\Desktop\Chanathivat_python\Project\Marathon.db')
                        c = conn.cursor()
                        ccc = input('Type [full/half/mini/funrun] ')
                        c.execute('SELECT * FROM  marathon WHERE typerun = "{}" ORDER BY timex'.format(ccc)) 
                        result = c.fetchall()
                        i=0
                        print('Rank {}'.format(ccc))
                        print('-'*64)
                        print('{0:<7}{1:<15}| {2:<15}| {3:<10}| {4:<10}|'.format('RANK | ','    NAME','     ID','  TYPE','  TIME'))
                        print('-'*64)
                        for x in result:
                            i+=1
                            print(' {0:<4}| {1:<15}| {2:<15}| {3:<10}| {4:<10}|'.format(i,x[1],x[3],x[6],x[9]))
                        print('-'*64,'\n')
                        conn.commit()
                        c.close()
                        showreme()                           
                    except:
                        print('ERROR!')
                def showrep():
                    try:
                        conn = sqlite3.connect(r'C:\Users\User\Desktop\Chanathivat_python\Project\Marathon.db')
                        c = conn.cursor()
                        ccc = input('Check ID card number ')
                        c.execute('SELECT * FROM  marathon WHERE ids = "{}" ORDER BY timex'.format(ccc)) 
                        x = c.fetchone()
                        print('Information of ID card number {}'.format(ccc))
                        print('\nNo\t{0:<8}\nID card number\t{3:<27}\nName - Surname\t{1:<15}{2:<15}\nRunning Type\t{4}\nTime\t{5}\n\n'.format(x[0],x[1],x[2],x[3],x[6],x[9]))
                        print('-'*64,'\n')
                        conn.commit()
                        c.close()
                        showreme()                           
                    except:
                        print('ERROR!')
                def showrea():
                    try:
                        conn = sqlite3.connect(r'C:\Users\User\Desktop\Chanathivat_python\Project\Marathon.db')
                        c = conn.cursor()
                        c.execute('SELECT * FROM  marathon ORDER BY timex') 
                        result = c.fetchall()
                        i=0
                        print('All Information ')
                        print('-'*64)
                        print('{0:<7}{1:<15}| {2:<15}| {3:<10}| {4:<10}|'.format('RANK | ','    NAME','     ID','  TYPE','  TIME'))
                        print('-'*64)
                        for x in result:
                            i+=1
                            print(' {0:<4}| {1:<15}| {2:<15}| {3:<10}| {4:<10}|'.format(i,x[1],x[3],x[6],x[9]))
                        print('-'*64,'\n')
                        conn.commit()
                        c.close()
                        showreme()                           
                    except:
                        print('ERROR!')
                if showa2 == 'a':
                    showrea()
                elif showa2 == 'b':
                    showrep()
                elif showa2 == 'c':
                    showre()
                elif showa2 == 'back':
                    show()                

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
                showreme()
            if showa == 'back':
                adminmenu()


        def edit():
            try:
                conn = sqlite3.connect(r'C:\Users\User\Desktop\Chanathivat_python\Project\Marathon.db')
                c = conn.cursor()
                iid = input('\nInsert ID card to be edited : ')
                c.execute('SELECT * FROM marathon WHERE ids = "{}"'.format(iid))
                r = c.fetchone()
                if not r:
                    print('No data found!\n')
                else:  
                    print ('\nNo\t{0:<8}\nName - Surname\t{1:<15}{2:<15}\nID card number\t{3:<27}\nGender\t{4}\nAge\t{5}\nRunning Type\t{6}\nEmail\t{7}\nPhone number\t{8}\n\n'.format(r[0],r[1],r[2],r[3],r[4],r[5],r[6],r[7],r[8]))      
                    ee1 = input('edit Name - Surname y/n ')
                    if ee1 == 'y':
                        fname,lname = input('Name - Surname >>> ').split()
                        datan = (fname,lname,'{}'.format(iid))
                        c.execute('''UPDATE marathon SET fname =?, lname =? WHERE ids =? ''',datan)
                    elif ee1 == 'n' :
                        pass
                    ee2 = input('edit Gender y/n ')
                    if ee2 == 'y':
                        sex = input('Gender >>> ')
                        datas = (sex,'{}'.format(iid))
                        c.execute('''UPDATE marathon SET sex =? WHERE ids =? ''',datas)
                    elif ee2 == 'n' :
                        pass 
                    ee3 = input('edit Age y/n ')
                    if ee3 == 'y':      
                        age = int(input('Age >>> '))
                        if type(age) == int:
                            dataa = (age,'{}'.format(iid))
                            c.execute('''UPDATE marathon SET age =? WHERE ids =? ''',dataa)                    
                        elif type(age) != int:
                            c.close()
                            edit()
                    elif ee3 == 'n' :
                        pass
                    ee4 = input('edit Type y/n ')
                    if ee4 =='y':
                        typerun = input('Type >>> ')
                        if typerun == 'full':
                            datat = (typerun,'{}'.format(iid))
                            c.execute('''UPDATE marathon SET typerun =? WHERE ids =? ''',datat)
                        elif typerun == 'half':
                            datat = (typerun,'{}'.format(iid))
                            c.execute('''UPDATE marathon SET typerun =? WHERE ids =? ''',datat)
                        elif typerun == 'mini':
                            datat = (typerun,'{}'.format(iid))
                            c.execute('''UPDATE marathon SET typerun =? WHERE ids =? ''',datat)
                        elif typerun == 'funrun':
                            datat = (typerun,'{}'.format(iid))
                            c.execute('''UPDATE marathon SET typerun =? WHERE ids =? ''',datat)
                        else:
                            c.close()
                            print('Something is wrong.')
                            edit()
                    elif ee4 == 'n' :
                        pass
                    ee5 = input('edit Email y/n ')
                    if ee5 == 'y':
                        email = input('Email >>> ')
                        datae = (email,'{}'.format(iid))
                        c.execute('''UPDATE marathon SET email =? WHERE ids =? ''',datae)
                    elif ee5 == 'n' :
                        pass
                    ee6 = input('edit Phone number y/n ')
                    if ee6 == 'y':
                        num = input('Phone number >>> ')
                        if len(num) == 10:
                            datann = (num,'{}'.format(iid))
                            c.execute('''UPDATE marathon SET num =? WHERE ids =? ''',datann)
                    elif ee6 == 'n' :
                        pass
                conn.commit()
                c.close()
        
                conn = sqlite3.connect(r'C:\Users\User\Desktop\Chanathivat_python\Project\Marathon.db')
                c = conn.cursor()
                c.execute('SELECT * FROM marathon WHERE ids = "{}"'.format(iid))
                b = c.fetchone()
                print ('\nNo\t{0:<8}\nName - Surname\t{1:<15}{2:<15}\nID card number\t{3:<27}\nGender\t{4}\nAge\t{5}\nRunning Type\t{6}\nEmail\t{7}\nPhone number\t{8}\n\n'.format(b[0],b[1],b[2],b[3],b[4],b[5],b[6],b[7],b[8]))      
                print('The information has been edited.\n')     
                c.close()
            except:
                print('\nERROR!\n')
        

        def edit2():
            try:
                conn = sqlite3.connect(r'C:\Users\User\Desktop\Chanathivat_python\Project\Marathon.db')
                c = conn.cursor()
                iid = input('\nInsert ID card to be edited : ')
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
                    print('The information has been edited.\n')
            except:
                print('\nERROR!\n')

        while True:
            adminmenu()
            if  choice2 == 'a':
                os.system('cls')
                dele()
            if choice2 == 'b':
                os.system('cls')
                show()
            if choice2 == 'e':
                os.system('cls')
                edit()
            elif choice2 == 'ea':
                os.system('cls')
                edit2()
            elif choice2 == 'exit':
                os.system('cls')
                print('\n-------------- Logged out -------------\n')
                break

while True:
    menu()
    if choice == 'a':
        os.system('cls')
        print('Enter the ID card number of 13 digits.')  
        add()
    elif choice == 'e':
        os.system('cls')
        editx()
    elif choice == 'b':
        os.system('cls')
        showx()
    elif choice == 'c':
        os.system('cls')
        showxx()
    elif choice == 'l':
        os.system('cls')
        admin()
    elif choice == 'exit':
        break