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

win.geometry("640x400")

win.resizable(False, False)

# frame - 위젯들 묶어주는 역할 (div같은 역할) - 위젯이 들어있지 않으면 표시가 안된다.
# side : top(기본값), left, right, bottom으로 이동
# anchor : 특정 위치로 이동(현재 구역내에서, center 포함 9개 위치)
# fill : 할당된 공간에 맞게 크기가 변경
# expand : 미사용공간을 모두 현재 위젯의 할당된 공간으로 변경
# justify : 정렬(좌, 우, 중앙)

# pack()은 grid()와 같이 사용할 수 없음.
frame1 = tk.Frame(win, bd=2, background='yellow')
# frame1.pack(side='left', fill='both') # 왼쪽에 붙어서 위젯 크기만큼 세로가 채워짐
# frame1.pack(side='left', fill='both', expand=True) # 나머지 공간 다 채움
# frame1.pack(side='left', fill='x', expand=True) # x방향으로만 채움
frame1.pack(side='left', fill='y', expand=True) # y방향으로만 채움

frame2 = tk.Frame(win, bd=2, background='blue')
# frame2.pack(fill='both') # 위젯 크기만큼 가로가 채워짐
# frame2.pack(side='right', fill='both') # 오른쪽에 붙어서 위젯 크기만큼 세로가 채워짐
frame2.pack(side='right', fill='both', expand=True) # frame1도 expand속성이 True이므로, frame1과 frame2가 반반 채워진다.

btn1 = tk.Button(frame1, text='프레임1')
btn1.pack()

btn2 = tk.Button(frame2, text='프레임2')
btn2.pack()

win.mainloop()