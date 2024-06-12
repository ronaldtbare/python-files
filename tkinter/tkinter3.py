# run and resize window to see effect.
from tkinter import *


root = Tk() # Tk() class creates our base window (root)

one = Label(root, text="One", bg="red", fg="white") # creates label
one.pack() # displays it in the window
two = Label(root, text="Two", bg="green", fg="black")
two.pack(fill=X) # fills up the X axis
three = Label(root, text="Three", bg="blue", fg="white")
three.pack(side=LEFT, fill=Y) # pushes to the left and fill up the Y axis

root.mainloop() # keeps the window on screen until closed