from buttons import button
from tkinter import *
root = Tk()

def Submit():
    name = Label(root,text="Hi "+ nameEntry.get()+"!")
    password = Label(root,text="Your password is: "+ passwordEntry.get())
    name.grid(row=3,column=0)
    password.grid(row=4,column=0)

# Labels and Entries
nameSection = Label(root,text="Username: ")
passwordSection = Label(root,text="Password: ")
nameEntry = Entry(root, width=50)
passwordEntry = Entry(root, width=50, show="*")

# Submit Button
submit = Button(root,text="Submit", command=Submit)

# Grid System
nameSection.grid(row=0,column=0)
nameEntry.grid(row=0,column=1)
passwordSection.grid(row=1,column=0)
passwordEntry.grid(row=1,column=1)
submit.grid(row=2,column=1)

root.mainloop()

# Entry usage and methods that might help 
# e = Entry(root, width=75,borderwidth=5, show="*", cursor="dot", justify=CENTER)
# width = int 
# borderwidth = int
# show = "str"
# cursor ="arrow" / "dot"
# justify = CENTER / LEFT / RIGHT
# e.get() -- to gather data
# e.insert(0, str) -- to put default text