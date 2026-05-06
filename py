from tkinter import *

root = Tk()
root.geometry("655x333")

def pure():
    print("YOUR INFORMATION HAS BEEN SUCCESSFULLY SAVED")

def hamp():
    print("DATA STORED SUCCESSFULLY")

def him():
    print("NAME STORED SUCCESSFULLY")

def her():
    print("COURSE NAME STORED SUCCESSFULLY")

f1 = Frame(root, bg="green", borderwidth=5, relief=SUNKEN, padx=10, pady=5)
f1.pack(side=RIGHT, fill=Y)

Button(f1, text="NAME", command=him).pack()
Button(f1, text="COURSE NAME", command=her).pack()
Button(f1, text="BRANCH", command=hamp).pack()
Button(f1, text="CONTINUE", command=pure).pack()

root.mainloop()
