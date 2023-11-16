import tkinter as tk

win = tk.Tk()

frame1 = tk.Frame(master=win, width=200, height=100, bg="Yellow")
# setting fill, side and expand
frame1.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True)

frame2 = tk.Frame(master=win, width=100, bg="blue")
frame2.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True)

frame3 = tk.Frame(master=win, width=50, bg="green")
frame3.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True)

win.mainloop()