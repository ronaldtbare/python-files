from tkinter import *

window = Tk() # Tk() class creates our base window
theLabel = Label(window, text = "This is too easy!") # defines the label
theLabel.pack() # packs the label inside the window to display it
window.mainloop() # keeps the window on screen until closed