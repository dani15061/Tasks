from tkinter import *

win = Tk() 
win.geometry("300x200") 

w = Label(win, text ='StudyTonight', font = "90",fg="Navyblue") 
w.pack() 
	
msg = Message(win, text = "Best place to learn coding online") 
	
msg.pack() 

win.mainloop() 