import tkinter as tk

# tkinter 패키지의 서브모듈 ttk를 가져옴
# ttk(themed tk를 의미) : 개선된 GUI를 제공하기 위한 모듈
from tkinter import ttk

win = tk.Tk()

win.title("파이썬 GUI")

ent1 = tk.Entry(win)
ent1.grid(row=0, column=0)

ent2 = tk.Entry(win)
ent2.grid(row=0, column=1)

# 체크버튼
chk1 = tk.Checkbutton(win, text="독서", state="disable") # 비활성화
chk1.grid(row=1, column=0, sticky='w') # 방향지정가능 : 동(e)서(w)남(s)북(n), 대각선도 가능(ne, se, sw, nw)

chk2 = tk.Checkbutton(win, text="운동")
chk2.select() # 체크한 상태로
chk2.grid(row=1, column=1, sticky=tk.E) # 이렇게도 사용할 수 있다.

chk3 = tk.Checkbutton(win, text="영화감상")
chk3.grid(row=1, column=2)

win.mainloop()