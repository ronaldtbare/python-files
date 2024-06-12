from tkinter import *

root = Tk() # Tk() class creates our base window

def leftClick(event):
    print("Left Click")

def middleClick(event):
    print("Middle Click")

def rightClick(event):
    print("Right Click")

frame = Frame(root, width=300, height=250) # the window will assume the size of the frame
frame.bind("<Button-1>", leftClick) # mouse click to see displays in console
frame.bind("<Button-2>", middleClick)
frame.bind("<Button-3>", rightClick)

frame.pack()

root.mainloop() # keeps the window on screen until closed