import tkinter as tk

# tkinter 패키지의 서브모듈 ttk를 가져옴
# ttk(themed tk를 의미) : 개선된 GUI를 제공하기 위한 모듈
from tkinter import ttk

win = tk.Tk()

win.title("파이썬 GUI")

def clickMe():
    label2.configure(text="하이! "+id.get())
    id.set("stop!!")

label = ttk.Label(win, text="아이디")
label.grid(row=0,column=0)

id = tk.StringVar() # 문자열을 담는 변수, int형은 IntVar()
entry1 = ttk.Entry(win, textvariable = id)
entry1.grid(row=0,column=1)

btn1 = ttk.Button(win, text="클릭", command=clickMe)
btn1.grid(row=0,column=2)

label2 = ttk.Label(win, text="")
label2.grid(row=1,column=1)

# 창 뜨자마자 포커스 주기
# entry1.focus()
btn1.focus()

win.mainloop()