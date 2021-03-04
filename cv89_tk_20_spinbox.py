## Spinbox 위젯

import tkinter as tk
from tkinter import scrolledtext

win = tk.Tk() # 윈도우 창 생성
win.title('파이썬 GUI - Spinbox') # 윈도우 이름 설정
win.geometry("600x400") # 윈도우 창 크기 설정
win.resizable(0, 0) # 윈도우 창 크기 고정

# 이벤트메소드
def _spin():
    val = spin.get()
    scroll.insert(tk.INSERT, val+'\n')

def _spin2():
    val = spin2.get()
    scroll.insert(tk.INSERT, val+'\n')

# Spinbox 클래스
spin = tk.Spinbox(win, width=5, from_=0, to=10, command=_spin) # 0~10 범위지정, 단위설정은 increment
spin.grid(row=0, column=0, padx=20, pady=20)

spin2 = tk.Spinbox(win, width=5, values=(10,20,40,100), command=_spin2) # 직접 범위지정
spin2.grid(row=0, column=1, padx=20, pady=20)

scroll = scrolledtext.ScrolledText(win, width=30, height=3, wrap=tk.WORD)
scroll.grid(row=1, columnspan=2, padx=20, pady=10)

win.mainloop() # 윈도우 창을 띄우려면 필요