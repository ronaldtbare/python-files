from tkinter import *
import random
from PIL import ImageTk,Image

root = Tk()
root.title('Dragon Dice')

def roll(number):
    die_choose = int(number)
    random_num = random.randint(1,die_choose)
    label_roll = Label(root,text=random_num, font=("Arial",50), padx=20, pady= 20)
    label_roll.grid(row=1, column=2)

def about():
    global about_window
    about_window = Toplevel()
    about_window.title("About")
    label1_top = Label(about_window, text="Dragon Dice v. 1.0", padx=10, pady=10).grid(row=0,column=0,padx=30, pady=10)
    label2_top = Label(about_window, text="by Travis Bare").grid(row=1,column=0)
    btn2 = Button(about_window, text="Close", command=about_window.destroy).grid(row=2, column=0,padx=10, pady=10)

# menubar definition
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About...", command=about)
menubar.add_cascade(label="Help", menu=helpmenu)

# die_sides = int(6)

title = ImageTk.PhotoImage(Image.open("images/dicebanner3.png"))

label1 = Label(root, image=title, padx=50, pady=50)
label1.grid(row=0, column=0, columnspan=3)

frame1 = LabelFrame(root, text="Choose your die to roll.", font=("Arial",12),padx=10,pady=10)
frame1.grid(row=1, column=0, columnspan=2, rowspan=2, padx=15, pady=15)


# a list of tuples
Dice = [
    ("D4 (four-sided)",4),
    ("D6 (six-sided)",6),
    ("D8 (eight-sided)",8),
    ("D10 (ten-sided)",10),
    ("D12 (twelve-sided)",12),
    ("D20 (twenty-sided)",20)
]

die = StringVar()  # uses strings instead of IntVar
die.set(20)

for text, number in Dice: # value should be different integer for each radiobutton
    Radiobutton(frame1, font=("Arial",12),text=text, variable=die, value=number).pack(anchor=W)

label_roll = Label(root,text="?", font=("Arial",50),padx=20, pady= 20)
label_roll.grid(row=1, column=2)

button_roll = Button(root, text="Roll",font=("Arial",25), command=lambda: roll(die.get()))
button_roll.grid(row=2,column=2, padx=20, pady=20)



root.config(menu=menubar) # activates menubar
root.mainloop()