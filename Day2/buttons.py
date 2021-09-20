from tkinter import *

root = Tk()

def button():
    text = Label(root, text="Clicked the button!")
    text.pack()

button_1 = Button(root, text="Click", padx=50, pady=30, command=button, fg="red",bg="black")
# state= DISABLED
# command = *function name*
# padx = *width*
# pady = *height*
# fg = "colourName" -- Font colour
# bg = "colurName" -- Background colour


button_1.pack()

root.mainloop()