import tkinter as tk

# tkinter 패키지의 서브모듈 ttk를 가져옴
# ttk(themed tk를 의미) : 개선된 GUI를 제공하기 위한 모듈
from tkinter import ttk

win = tk.Tk()

win.title("파이썬 GUI")

def select():
    label3.configure(text=fruitName.get() + '를/을 ' + amount.get() + '개 선택하셨습니다')

label1 = ttk.Label(win, text="과일명 입력:")
label1.grid(row=0,column=0)

fruitName = tk.StringVar() # 문자열을 담는 변수, int형은 IntVar()
entry1 = ttk.Entry(win, width=15, textvariable=fruitName) # width속성을 통해 가로크기 조절
entry1.grid(row=1,column=0)

label2 = ttk.Label(win, text="수량 선택:")
label2.grid(row=0,column=1)

amount = tk.StringVar()
combo = ttk.Combobox(win, width=10, textvariable=amount)
combo.grid(row=1,column=1)
combo['values'] = (1,2,3,4,5) # or [1,2,3,4,5]

btn1 = ttk.Button(win, text="확인", command=select)
btn1.grid(row=1,column=2)

label3 = ttk.Label(win, text="")
label3.grid(row=2,column=0)

# 창 뜨자마자 포커스 주기
entry1.focus()
# btn1.focus()

win.mainloop()