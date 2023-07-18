from tkinter import *
from tkinter import messagebox

# creating the object
root=Tk()

# resolution of the window
root.geometry("750x400")

root.config(bg='#80ffff')

# Enabling the resize feature
root.resizable(True, True)

def go_to_update():
    import update
    #execfile('update.py')
    
def go_to_appointment():
    import appointment
    #execfile('appointment.py')

# labels for the window
heading = Label(root,
                text="What Do You Want To do?",
                font=('arial 40 bold'),
                fg='black',
                bg='#80ffff').place(x=0, y=0)

#Buttons to perform command
update_app=Button(root,
                    text='Update existing Appointment',
                    width=40,
                    height=2,
                    font=25,
                    bg='darkgreen',
                    fg='yellow',
                    command = go_to_update).place(x=50,
                                                    y=120)

create_app=Button(root,
                    text='Create new Appointment',
                    width=40,
                    height=2,
                    font=25,
                    bg='darkgreen',
                    fg='yellow',
                    command = go_to_appointment).place(x=50,
                                                    y=230)

root.mainloop()







