# import modules
from tkinter import *
import sqlite3
import tkinter.messagebox
import re
# connect to the databse.
conn = sqlite3.connect('database.db')
# cursor to move around the databse
c = conn.cursor()

# empty list to later append the ids from the database
ids = []

# tkinter window
class Application:
    def __init__(self, master):
        self.master = master

        # creating the frames in the master
        self.left = Frame(master, width=800, height=720, bg='lightyellow')
        self.left.pack(side=LEFT)

        self.right = Frame(master, width=400, height=720, bg='steelblue')
        self.right.pack(side=RIGHT)

        # labels for the window
        self.heading = Label(self.left, text="AAK Hospital Appointments", font=('arial 40 bold'), fg='black', bg='lightyellow')
        self.heading.place(x=0, y=0)
        # patients name
        self.name = Label(self.left, text="Patient's Name", font=('arial 18 bold'), fg='black', bg='lightyellow')
        self.name.place(x=0, y=100)

        # age
        self.age = Label(self.left, text="Age", font=('arial 18 bold'), fg='black', bg='lightyellow')
        self.age.place(x=0, y=140)

        # gender
        self.gender = Label(self.left, text="Gender", font=('arial 18 bold'), fg='black', bg='lightyellow')
        self.gender.place(x=0, y=180)

        # phone
        self.phone = Label(self.left, text="Phone Number", font=('arial 18 bold'), fg='black', bg='lightyellow')
        self.phone.place(x=0, y=220)

        # Doctor's name
        self.docname = Label(self.left, text="Doctor's Name", font=('arial 18 bold'), fg='black', bg='lightyellow')
        self.docname.place(x=0, y=260)

        # Doctor's Specialization
        self.docsp = Label(self.left, text="Doctor's Specialization", font=('arial 18 bold'), fg='black', bg='lightyellow')
        self.docsp.place(x=0, y=300)

        # appointment time
        self.time = Label(self.left, text="Appointment Time", font=('arial 18 bold'), fg='black', bg='lightyellow')
        self.time.place(x=0, y=340)


        # Entries for all labels============================================================
        self.name_ent = Entry(self.left, width=30)
        self.name_ent.place(x=300, y=100)

        self.age_ent = Entry(self.left, width=30)
        self.age_ent.place(x=300, y=140)
    
        self.gender_ent = Entry(self.left, width=30)
        self.gender_ent.place(x=300, y=180)

        self.phone_ent = Entry(self.left, width=30)
        self.phone_ent.place(x=300, y=220)

        self.docname_ent = Entry(self.left, width=30)
        self.docname_ent.place(x=300, y=260)

        self.docsp_ent = Entry(self.left, width=30)
        self.docsp_ent.place(x=300, y=300)

        self.time_ent = Entry(self.left, width=30)
        self.time_ent.place(x=300, y=340)


        # button to perform a command
        self.submit = Button(self.left, text="Add Appointment", width=20, height=2, bg='steelblue', command=self.add_appointment)
        self.submit.place(x=300, y=380)
    
        # getting the number of appointments fixed to view in the log
        c.execute("select * from appointments") 
        
        self.totalapp = len(c.fetchall())
        # displaying the logs in our right frame
        self.logs = Label(self.right, text="Logs", font=('arial 28 bold'), fg='white', bg='steelblue')
        self.logs.place(x=0, y=0)

        self.box = Text(self.right, width=50, height=40)
        self.box.place(x=20, y=60)
        self.box.insert(END, "Total Appointments till now :  " + str(self.totalapp))
    # funtion to call when the submit button is clicked
    def add_appointment(self):
        # getting the user inputs
        self.val1 = self.name_ent.get()
        self.val2 = self.age_ent.get()
        self.val3 = self.gender_ent.get()
        self.val4 = self.phone_ent.get()
        self.val5 = self.docname_ent.get()
        self.val6 = self.docsp_ent.get()
        self.val7 = self.time_ent.get()

        #regex code to check the input given
        no_check=re.compile("[6-9][0-9]{9}")
        age_check=re.compile("[1-9][0-9]?")

        # checking if the user input is empty
        if self.val1 == '' or self.val2 == '' or self.val3 == '' or self.val4 == '' or self.val5 == '' or self.val6 == '' or self.val7 == '':
            tkinter.messagebox.showinfo("Warning", "Please Fill Up All Boxes")
        elif ((no_check.match(self.val4)==0) or (len(self.val4)!=10)):
            tkinter.messagebox.showinfo("Warning", "Please enter a valid number")
        elif ((age_check.match(self.val2)==0) or (len(self.val2)<3)):
            tkinter.messagebox.showinfo("Warning", "Please enter a valid age")
        else:
            # now we add to the database
            sql = "INSERT INTO 'appointments' (name, age, gender, phone, docname, docsp, time) VALUES(?, ?, ?, ?, ?, ?, ?)"
            c.execute(sql, (self.val1, self.val2, self.val3, self.val4, self.val5, self.val6, self.val7))
            conn.commit()
            tkinter.messagebox.showinfo("Success", "Appointment for " +str(self.val1) + " has been created ")
            

            self.box.insert(END, '\nAppointment fixed for ' + str(self.val1) + ' at ' + str(self.val5))

# creating the object
root = Tk()
b = Application(root)

# resolution of the window
root.geometry("1200x720+0+0")

# enabling the resize feature
root.resizable(True, True)

# end the loop
root.mainloop()


