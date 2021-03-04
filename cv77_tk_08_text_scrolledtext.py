import tkinter as tk
from tkinter import scrolledtext

# tkinter 패키지의 서브모듈 ttk를 가져옴
# ttk(themed tk를 의미) : 개선된 GUI를 제공하기 위한 모듈
from tkinter import ttk

win = tk.Tk()

win.title("파이썬 GUI")

colors = ['Blue','Yellow','Red']
# color1 = 'Blue'
# color2 = 'Yellow'
# color3 = 'Red'

def selColor():
    radioVal = radioColor.get()
    for i in range(3):
        if radioVal == i:
            win.configure(background=colors[i])

radioColor = tk.IntVar()

for col in range(3):
    rad = tk.Radiobutton(win, text=colors[col], variable=radioColor, value=col, command=selColor)
    rad.grid(row=0, column=col, sticky='w')

txtComments = tk.Text(win)
txtComments.grid(row=1,column=0)

# 스크롤이 생김
txtComments = scrolledtext.ScrolledText(win, width=100, height=3, wrap='word')
# txtComments.grid(row=2,column=0)
txtComments.grid(column=0, columnspan=3) # 열합치기


win.mainloop()