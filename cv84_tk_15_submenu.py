## 메뉴안에 서브메뉴

import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.geometry("640x400")
win.resizable(False, False)

menu_bar = tk.Menu(win)
menu1 = tk.Menu(win, tearoff=0)
submenu = tk.Menu(win, tearoff=0)
submenu.add_radiobutton(label='Option1')
submenu.add_radiobutton(label='Option2')

# 메뉴에 연결
menu_bar.add_cascade(label='Menu 1', menu=menu1)
menu1.add_cascade(label='Submenu', menu=submenu)

# 메뉴가 화면에 보이도록 등록
win.config(menu=menu_bar)

win.mainloop()