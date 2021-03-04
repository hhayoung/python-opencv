import tkinter as tk

win = tk.Tk()

win.geometry("640x400")

win.resizable(False, False)

# place
btn1 = tk.Button(win, text='btn1')
btn1.place(x=100,y=100)

btn2 = tk.Button(win, text='btn2')
btn2.place(x=100,y=200, width=150, height=150)

btn3 = tk.Button(win, text='btn3', bg='pink') # background = bg
# btn3.place(x=300,rely=0.2) #
btn3.place(x=0, relx=0.5,rely=0.5) # relx, rely : x,y좌표 배치비율(0~1사이)

btn4 = tk.Button(win, text='btn4')
# btn4.place(x=0, y=200, relwidth=1) # relwidth : 전체 다 차지
# btn4.place(x=0, y=200, relwidth=0.8) # relwidth : 80% 차지
btn4.place(x=0, y=200, relwidth=0.8, relheight=0.1) # relwidth, relheight : 위젯의 너비,높이 비율(0~1사이)

win.mainloop()