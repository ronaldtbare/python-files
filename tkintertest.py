import tkinter as tk

root = tk.Tk()
root.title("Simple App")

def on_click():
    lbl.config(text="Button Clicked!")


lbl = tk.Label(root, text="Label 1") 
lbl.grid(row=1, column=0)

# print(lbl.config().keys()) # prints all keys for widget

btn = tk.Button(root, text="Button 1", command=on_click) # create the button
btn.grid(row=1, column=1) # draw on window

root.mainloop()