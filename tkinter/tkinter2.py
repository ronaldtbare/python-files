from tkinter import *

root = Tk() # Tk() class creates our base window (root)

topFrame = Frame(root)
topFrame.pack()

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text="Button 1", fg="red")
button2 = Button(topFrame, text="Button 2", fg="blue")
button3 = Button(topFrame, text="Button 3", fg="green")
button4 = Button(bottomFrame, text="Button 4", fg="purple")

button1.pack(side=LEFT)
button2.pack(side=LEFT) # button1 is in the way so it goes left as much as it can
button3.pack(side=LEFT) # button1 and button2 in way...ditto
button4.pack(side=BOTTOM)


root.mainloop() # keeps the window on screen until closed