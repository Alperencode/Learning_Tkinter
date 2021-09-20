from tkinter import *

root = Tk()

# Our labels
label_1 = Label(root, text="Hello World")
label_2 = Label(root, text="Learning Tkinter")

# # Its just packing the whole thing
# label_1.pack()
# # Probably not using this while doing a project but its quick way to see whats happening in basics

# rows and columns starts with zero (0)
label_1.grid(row=0, column=0)   
label_2.grid(row=1, column=0)
# Made a simple two text which is on same column but different rows 


root.mainloop() # to make root the mainloop 