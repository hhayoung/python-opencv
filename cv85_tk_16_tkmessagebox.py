import tkinter as tk
from tkinter import messagebox as msg

# tkMessageBox

win = tk.Tk()
win.geometry("640x400")
win.resizable(False, False)

def hello():
    # msg.showinfo('파이썬 GUI 정보', '파이썬 강좌') # 제목, 내용 => info라서 아이콘은 i 
    # msg.showwarning('경고메세지', '파이썬 GUI 경고 메시지 입니다') # => 경고라서 아이콘도 주의 표시
    # msg.showerror('에러메세지', '파이썬 GUI 에러 메시지 입니다') # => 에러라서 아이콘 x
    # msg.askokcancel('멀티 선택메세지', '파이썬 GUI 프로그래밍 입니다') # => 확인, 취소 버튼 (True, None)
    msg.askyesnocancel('멀티 선택메세지', '파이썬 GUI 프로그래밍 입니다') # => 예, 아니요, 취소 버튼 (True, False, None)

btn1 = tk.Button(win, text='Hello world!', command=hello)
btn1.pack()

def displayInfo():
    msg.showinfo('help 메뉴', '파이썬 GUI 공부하기')

menu_bar = tk.Menu(win)
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_radiobutton(label='About', command=displayInfo)


# 메뉴에 연결
menu_bar.add_cascade(label='help', menu=help_menu)

# 메뉴가 화면에 보이도록 등록
win.config(menu=menu_bar)


win.mainloop()