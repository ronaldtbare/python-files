from tkinter import *
import random
# from PIL import ImageTk,Image

root = Tk()
root.title('Dragon Dice')

def roll(number):
    die_choose = int(number)
    random_num = random.randint(1,die_choose)
    label_roll = Label(root,text=random_num, font=("Arial",35),padx=20, pady= 20)
    label_roll.grid(row=3, column=1)


die_sides = int(6)

label1 = Label(root, text="Dragon Dice", font=("Arial", 25), padx=50,pady=50)
label1.grid(row=0, column=0, columnspan=3)

frame1 = LabelFrame(root, text="Choose your die to roll.")
frame1.grid(row=1, column=0, columnspan=3)


# a list of tuples
Dice = [
    ("D4",4),
    ("D6",6),
    ("D8",8),
    ("D10",10),
    ("D12",12),
    ("D20",20)
]

die = StringVar()  # uses strings instead of IntVar
die.set(6)

for text, number in Dice:
    Radiobutton(frame1, text=text, variable=die, value=number).pack(anchor=W)

label_roll = Label(root,text="?", font=("Arial",35), padx=20, pady= 20)
label_roll.grid(row=3, column=1)

button_roll = Button(root, text="Roll", command=lambda: roll(die.get()))
button_roll.grid(row=4,column=1, padx=20, pady=20)

root.mainloop()