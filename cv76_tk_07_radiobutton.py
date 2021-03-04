import tkinter as tk

# tkinter 패키지의 서브모듈 ttk를 가져옴
# ttk(themed tk를 의미) : 개선된 GUI를 제공하기 위한 모듈
from tkinter import ttk

win = tk.Tk()

win.title("파이썬 GUI")

color1 = 'Blue'
color2 = 'Yellow'
color3 = 'Red'

def sel_rbtn():
    radioVal = radioColor.get()
    if radioVal == 1:
        label.configure(background=color1)
    elif radioVal == 2:
        label.configure(background=color2)
    elif radioVal == 3:
        label.configure(background=color3)

radioColor = tk.IntVar()
radio1 = tk.Radiobutton(win, text=color1, value=1, variable=radioColor, command=sel_rbtn) # radioColor에 value값이 들어감.
radio1.grid(row=0,column=0, sticky='w')

radio2 = tk.Radiobutton(win, text=color2, value=2, variable=radioColor, command=sel_rbtn)
radio2.grid(row=0,column=1, sticky='w')

radio3 = tk.Radiobutton(win, text=color3, value=3, variable=radioColor, command=sel_rbtn)
radio3.grid(row=0,column=2, sticky='w')

label = tk.Label(win, width=50)
label.grid(row=0,column=3)

win.mainloop()