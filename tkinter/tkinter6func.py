# How to activate a function with a widget

from tkinter import *

root = Tk() # Tk() class creates our base window

def printHello():
    print("Hello!")

def printBye(event):
    print("Goodbye!")


# this binds a function to a widget with the command property
button_1 = Button(root, text="Say Hello", command=printHello)
button_1.pack()

button_2 = Button(root, text="Say Bye")
button_2.bind("<Button-1>", printBye) # first arg is left mouse  button, second arg in function
button_2.pack()


root.mainloop() # keeps the window on screen until closed