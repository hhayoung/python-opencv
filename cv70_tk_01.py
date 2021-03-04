# 파이썬 GUI 프레임워크(Toolkit)

# Tkinter(Tk interface) : 파이썬에서 기본적으로 제공되는 표준 라이브러리
# PyQt

import tkinter as tk

# Tk 클래스를 이용해서 윈도우 창을 생성
win = tk.Tk()

# 파이썬 tkinter 위젯 클래스 중에 Label, Button
label = tk.Label(win, text="welcome to python")
button = tk.Button(win, text="클릭")

label.pack() # pack: 고정시키겠다
button.pack()

# 이벤트 루프를 생성
win.mainloop() # -> 이 코드가 있어야 창이 뜬다. 
# 위젯을 넣지 않았을 때는 기본 크기로 창이 만들어지고,
# 위젯을 넣으면 위젯크기로 크기가 설정이 된다. 