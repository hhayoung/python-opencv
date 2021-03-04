# Geometry Manager
# Tkinter 에서는 위젯들을 화면에 배치하는 방식으로 3가지 방식을 사용한다.

# Pack : 위젯들을 상하로 패킹(pack()메소드)
#        불필요한 공간을 없애고 사용

# Grid : 위젯들을 격자(테이블)에 배치하는 방식(grid()메소드)

# Place(absolute) : 절대 좌표로 위젯을 정하여 배치(place()메소드)
#                   윈도우 크기 변경에 따라 위젯들이 변경되지 않는다. 많이 사용되지 않음.

import tkinter as tk
from tkinter import ttk

win = tk.Tk()

# win.geometry("400x400") # "가로x세로" 형태의 문자열로 적어야 한다.
win.geometry("400x400+1000+200") # "가로x세로" 형태의 문자열로 적어야 한다.
# 윈도우의 크기를 설정할 수 있다.

label = tk.Label(win, text="파이썬 파이썬\n파이썬", background="yellow", width="20", height="5", bd=5, relief="solid", anchor=tk.NE, justify=tk.LEFT) 
# 이때의 height가 세로가 아니라 5줄이 표현되는 것 같음.
# bd : border 두께. 뒤에 속성들이 온다.
# 텍스트의 위치를 조정하고 싶을 때, anchor 속성 사용(E,W,S,N,SE,SW,NE,NW), center도 있어서 총 9개
# 여려 줄이 있는 텍스트를 정렬하고 싶을 때, justify 속성 사용(tk.LEFT, tk.RIGHT, tk.CENTER)
label.pack() # geometry가 설정되었기 때문에 윈도우창에 크기가 label에 맞춰지지 않음.

win.mainloop()