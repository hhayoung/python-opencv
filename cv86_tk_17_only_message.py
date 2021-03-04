import tkinter as tk
from tkinter import messagebox as msg

# 메세지 창만 열어보기

win = tk.Tk()
win.geometry("640x400")
win.resizable(False, False)

win.withdraw() # 기존 창을 닫고, 메시지창만 화면에 보이게 

msg.showinfo('파이썬 메시지 창', '메시지 창만 열어보겠습니다')


win.mainloop()