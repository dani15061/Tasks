from tkinter import *
win = Tk() 
win.geometry("200x200") 

v = StringVar(win, "1") 

options = {" Option A" : "1", 
		"Option B" : "2", 
		"Option C" : "3", 
		"Option D" : "4" 
		} 

for (txt, val) in options.items(): 
	Radiobutton(win, text=txt, variable=v, value=val).pack(side = TOP, ipady = 4) 

mainloop() 