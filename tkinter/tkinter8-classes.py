from tkinter import *


class MyButtons:
    def __init__(self, master): # master is the the root gui window
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame, text="Print Message", command=self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quoteButton = Button(frame, text="Print Quote", command=self.printQuote)
        self.quoteButton.pack(side=LEFT)

        # frame.quit breaks main loop and ends program
        self.quitButton = Button(frame, text="Quit!", command=frame.quit)  
        self.quitButton.pack(side=LEFT)

    def printMessage(self):
        print("Wow, this works.")

    
    def printQuote(self):
        print("The teacher appears when the student is ready.")

root = Tk() # Tk() class creates our base window

x = MyButtons(root)


root.mainloop() # keeps the window on screen until closed