import tkinter as tk
from tkinter import ttk

win = tk.Tk()

win.geometry("640x400")

win.resizable(False, False)

lbFrame1 = ttk.LabelFrame(win, text='라벨 프레임1')
lbFrame1.grid(row=0,column=0, padx=20, pady=20)

name = tk.StringVar()
ttk.Label(lbFrame1, text='과일명').grid(row=0,column=0)
ttk.Entry(lbFrame1, width=12, textvariable=name).grid(row=1, column=0, padx=10)

ttk.Label(lbFrame1, text='수량').grid(row=0,column=1)
number = tk.IntVar()
ttk.Entry(lbFrame1, width=10, textvariable=number).grid(row=1,column=1,padx=10)

lbFrame2 = ttk.LabelFrame(lbFrame1, text='라벨 프레임2')
lbFrame2.grid(row=2,column=0, padx=20, pady=20, columnspan=2)

ttk.Label(lbFrame2, text='Label1').grid(row=0,column=0,sticky='w')
ttk.Label(lbFrame2, text='Label2').grid(row=1,column=0,sticky='w')
ttk.Label(lbFrame2, text='Label3').grid(row=2,column=0,sticky='w')
# -> 간격 너무 오밀조밀. 한꺼번에 여백 조정을 하고 싶을 때

# winfo_children() : 자식의 목록을 반환하는 함수
for child in lbFrame2.winfo_children():
    child.grid_configure(padx=20, pady=10)


win.mainloop()