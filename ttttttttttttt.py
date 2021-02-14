from tkinter import *
import sqlite3

root =Tk()
root.title('Student information')
root.geometry('400x400')

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
# Create Submit Function For database
def submit():
    conn = sqlite3.connect(r'C:\Users\User\Desktop\Chanathivat_python\Student.db')
    c = conn.cursor()
    c.execute('INSERT INTO students VALUES (:id,:fname, :lname, :email, :sex, :age, :year)',
            {
                'id': id.get(),
                'fname': fname.get(),
                'lname': lname.get(),
                'email': email.get(),
                'sex': sex.get(),
                'age': age.get(),
                'year': year.get()
            })
    conn.commit()
    conn.close()

    fname.delete(0, END)
    lname.delete(0, END)
    email.delete(0, END)
    sex.delete(0, END)
    age.delete(0, END)
    year.delete(0, END)

# Create Text Boxes
fname = Entry(root, width=30)
fname.grid(row=0, column=1, padx=20)
lname = Entry(root, width=30)
lname.grid(row=1, column=1)
email = Entry(root, width=30)
email.grid(row=2, column=1)
sex = Entry(root, width=30)
sex.grid(row=3, column=1)
age = Entry(root, width=30)
age.grid(row=4, column=1)
year = Entry(root, width=30)
year.grid(row=5, column=1)

# Create Text Box Labels
fname_label = Label(root, text='First Name')
fname_label.grid(row=0, column=0)
lname_label = Label(root, text='Last Name')
lname_label.grid(row=1, column=0)
email_label = Label(root, text='Email')
email_label.grid(row=2, column=0)
sex_label = Label(root, text='Sex')
sex_label.grid(row=3, column=0)
age_label = Label(root, text='Age')
age_label.grid(row=4, column=0)
year_label = Label(root, text='Year')
year_label.grid(row=5, column=0)

# Create Submit Button
submit_btn = Button(root, text='Add Student', command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, ipadx=100)
conn.commit()
conn.close()
root.mainloop()