## 상단에 메뉴 만들기

import tkinter as tk
from tkinter import ttk

# Menu 만들기
# 메뉴 이름 = tk.Menu(윈도우창) : 해당 윈도우 창에 메뉴를 사용할 수 있음.
# 윈도우 창.config(menu=메뉴 이름) : 해당 윈도우 창에 메뉴를 등록해야 한다.

win = tk.Tk()
win.geometry("640x400")
win.resizable(False, False)

menu_bar = tk.Menu(win)
win.config(menu=menu_bar)

# 메뉴바에 각각의 메뉴가 보이도록
file_menu = tk.Menu(menu_bar, tearoff=0) # 점선 사라짐
file_menu.add_command(label="서브메뉴1")
file_menu.add_command(label="서브메뉴2")
file_menu.add_separator() # 구분선
file_menu.add_command(label="종료", command=win.quit)
# 상위 메뉴와 하위 메뉴 연결(label='메뉴이름', menu='연결할 하위메뉴')
menu_bar.add_cascade(label='File', menu=file_menu)

# 메뉴바에 각각의 메뉴가 보이도록
rad_menu = tk.Menu(menu_bar, tearoff=0) # 점선 사라짐
rad_menu.add_radiobutton(label="서브메뉴1", state='disable')
rad_menu.add_radiobutton(label="서브메뉴2")
rad_menu.add_radiobutton(label="서브메뉴3")
menu_bar.add_cascade(label='라디오메뉴', menu=rad_menu)


win.mainloop()