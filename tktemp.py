#  Tkinter simple temperature converter

import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Temperature Converter")

# Set geometry(width x height)
window.geometry('350x350')


def fahrenheit():
    # F=C× 5/9 +32
    temp = float(txt.get())
    conv_f = temp * (5/9) + 32
    formatted = f'{conv_f:.1f}\u00B0F'
    convlbl2.configure(text=formatted)
  

def celsius():
    # °C=(°F−32)× 9/5
    temp = float(txt.get())
    conv_c = (temp - 32) * (5/9)
    formatted = f'{conv_c:.1f}\u00B0C'
    convlbl2.configure(text=formatted)
    

def clear():
    convlbl2.configure(text="?")
    txt.delete(0, tk.END)
   

# adding a label to the root window
lbl = tk.Label(window, text = "Enter your temperature: ")
lbl.grid(padx=10, pady=30, column=0, row=1)

# adding Entry field
txt = tk.Entry(window, width=10)
txt.grid(column=1, row=1)

# adding a label to the root window
convlbl1 = tk.Label(window, text = "Your converted temperature is: ")
convlbl1.grid(padx=10, pady=20, column=0, row=2)

# adding a label to the root window
convlbl2 = tk.Label(window, fg="red", text = "?")
convlbl2.grid(padx=10, pady=20, column=1, row=2)

# fahrenheit button
fahrbtn = tk.Button(window, text = "Fahrenheit", fg = "blue", command=fahrenheit)
fahrbtn.grid(pady=30, column=0, row=3)

# celsius button
celbtn = tk.Button(window, text = "Celsius", fg = "green",command=celsius)
celbtn.grid(pady=30, column=1, row=3)

# clear button
clrbtn = tk.Button(window, text = "Clear", fg = "black",command=clear)
clrbtn.grid(pady=30, column=1, row=4)


# Execute Tkinter (run it)
window.mainloop()