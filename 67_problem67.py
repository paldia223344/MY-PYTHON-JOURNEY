from tkinter import*
root = Tk()

root.geometry("666x333")

f1 = Frame(root, borderwidth = 8 , bg = "purple", relief = SUNKEN , width = 100 , height = 200)
f1.pack(side = LEFT, anchor = "n")

b1 = Button(f1, bg = "red", text = "Click Me")
b1.pack(pady = 10, side = LEFT ,padx = 10)

b2 = Button(f1, bg = "red", text = "Click Me")
b2.pack(pady = 10, side = LEFT ,padx = 10)

root.mainloop()
