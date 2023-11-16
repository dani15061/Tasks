from tkinter import *
win = Tk()
win.title("Calculator")
win.geometry("600x510")
win.resizable(0,0)

def btn_click(item):
    global expression
    expression = expression + str(item)
    input.set(expression)

def bt_clear(): 
    global expression 
    expression = "" 
    input.set("") 
 
def bt_equal():
    global expression
    result = str(eval(expression)) 
    input.set(result)
    expression = ""

expression = ""
input = StringVar()
input_frame = Frame(win,width = 312, height=50, bd=0,highlightbackground="black", highlightcolor="black", highlightthickness=2)
input_frame.pack(side=TOP)
input_field = Entry(input_frame,font=('arial',20,'bold') ,textvariable=input, width = 50,bg='#eee', bd=0,justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=20)
btn_frame = Frame(win,width=312,height=272.5,bg='white')
btn_frame.pack()

clear = Button(btn_frame, text = "C", fg = "white", width = 62, height = 5, bd = 0, bg = "black", cursor = "hand2", command = lambda: bt_clear()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)
divide = Button(btn_frame, text = "/", fg = "white", width = 20, height = 5, bd = 0, bg = "black", cursor = "hand2", command = lambda: btn_click("/")).grid(row = 0, column = 3, padx = 1, pady = 1)
seven = Button(btn_frame, text = "7", fg = "white", width = 20, height = 5, bd = 0, bg = "black", cursor = "hand2", command = lambda: btn_click(7)).grid(row = 1, column = 0, padx = 1, pady = 1)
eight = Button(btn_frame, text = "8", fg = "white", width = 20, height = 5, bd = 0, bg = "black", cursor = "hand2", command = lambda: btn_click(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
nine = Button(btn_frame, text = "9", fg = "white", width = 20, height = 5, bd = 0, bg = "black", cursor = "hand2", command = lambda: btn_click(9)).grid(row = 1, column = 2, padx = 1, pady = 1)
multiply = Button(btn_frame, text = "*", fg = "white", width = 20, height = 5, bd = 0, bg = "black", cursor = "hand2", command = lambda: btn_click("*")).grid(row = 1, column = 3, padx = 1, pady = 1)
four = Button(btn_frame, text = "4", fg = "white", width = 20, height = 5, bd = 0, bg = "black", cursor = "hand2", command = lambda: btn_click(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
five = Button(btn_frame, text = "5", fg = "white", width = 20, height = 5, bd = 0, bg = "black", cursor = "hand2", command = lambda: btn_click(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
six = Button(btn_frame, text = "6", fg = "white", width = 20, height = 5, bd = 0, bg = "black", cursor = "hand2", command = lambda: btn_click(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
minus = Button(btn_frame, text = "-", fg = "white", width = 20, height = 5, bd = 0, bg = "black", cursor = "hand2", command = lambda: btn_click("-")).grid(row = 2, column = 3, padx = 1, pady = 1)
one = Button(btn_frame, text = "1", fg = "white", width = 20, height = 5, bd = 0, bg = "black", cursor = "hand2", command = lambda: btn_click(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
two = Button(btn_frame, text = "2", fg = "white", width = 20, height = 5, bd = 0, bg = "black", cursor = "hand2", command = lambda: btn_click(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
three = Button(btn_frame, text = "3", fg = "white", width = 20, height = 5, bd = 0, bg = "black", cursor = "hand2", command = lambda: btn_click(3)).grid(row = 3, column = 2, padx = 1, pady = 1)
plus = Button(btn_frame, text = "+", fg = "white", width = 20, height = 5, bd = 0, bg = "black", cursor = "hand2", command = lambda: btn_click("+")).grid(row = 3, column = 3, padx = 1, pady = 1)
zero = Button(btn_frame, text = "0", fg = "white", width = 41, height = 5, bd = 0, bg = "black", cursor = "hand2", command = lambda: btn_click(0)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
point = Button(btn_frame, text = ".", fg = "white", width = 20, height = 5, bd = 0, bg = "black", cursor = "hand2", command = lambda: btn_click(".")).grid(row = 4, column = 2, padx = 1, pady = 1)
equals = Button(btn_frame, text = "=", fg = "white", width = 20, height = 5, bd = 0, bg = "black", cursor = "hand2", command = lambda: bt_equal()).grid(row = 4, column = 3, padx = 1, pady = 1)
 
win.mainloop()

