import tkinter
from tkinter import *


top = Tk()
top.geometry("300x150")

a = Button(top, text="yellow", activeforeground="black", activebackground="yellow", pady=10)
b = Button(top, text="Blue", activeforeground="black", activebackground="blue", pady=10)
c = Button(top, text="Green", activeforeground = "black", activebackground="green", pady=10)
d = Button(top, text="red", activeforeground="black", activebackground="red", pady=10)

a.pack(side = LEFT)
b.pack(side = RIGHT)
c.pack(side = TOP)
d.pack(side = BOTTOM)
top.mainloop()