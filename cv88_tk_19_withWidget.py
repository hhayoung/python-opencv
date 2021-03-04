## 종합

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import scrolledtext

win = tk.Tk()
win.geometry("640x400")
win.resizable(False, False)

tabControl = ttk.Notebook(win)

# 첫번째 탭
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Tab 1')

# 두번째 탭
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text='Tab 2')

# 위치시키기
tabControl.pack(fill='both', expand=True, padx=10, pady=10)

# 각 탭에 내용 넣기
lbFrame1 = ttk.LabelFrame(tab1, text='파이썬 GUI 1')
lbFrame1.grid(row=0,column=0, padx=20, pady=20)

## Tab1 내용
def select_fruit():
    txtComments.insert(tk.INSERT, fruitName.get() + '를/을 ' + amount.get() + '개 선택하셨습니다')

ttk.Label(lbFrame1, text='과일명 입력').grid(row=0, column=0, sticky=tk.W)
fruitName = tk.StringVar()
ttk.Entry(lbFrame1, width=10, textvariable=fruitName).grid(row=1, column=0)

ttk.Label(lbFrame1, text='수량').grid(row=0, column=1)
amount = tk.StringVar()
combo = ttk.Combobox(lbFrame1, width=12, textvariable=amount)
combo['values'] = [1,2,5,10,20,30] # grid를 먼저 하면 안 됨.
combo.grid(row=1,column=1) # values 설정하고 난 다음에 위치 시켜야 함.
combo.current(0) # 리스트중에 몇번째를 초기에 보여줄건지

ttk.Button(lbFrame1, text='확인', command=select_fruit).grid(row=1, column=2)

txtComments = scrolledtext.ScrolledText(lbFrame1, width=40, height=3, wrap='word')
txtComments.grid(row=2, column=0, columnspan=3, padx=5, pady=5)
# -> 무조건 grid를 이용해 위젯을 위치시키기 전에 모든 동작을 한 뒤에 위치시켜야 한다. 한 줄에 쭉 쓰면 안 됨.

## Tab2 내용
def selColor():
    radioVal = radioColor.get()
    for i in range(3):
        if radioVal == i:
            color.config(text=colors[i])

lbFrame2 = ttk.LabelFrame(tab2, text='파이썬 GUI 2')
lbFrame2.grid(row=0,column=0, padx=20, pady=20)

# 체크박스
chk1 = tk.Checkbutton(lbFrame2, text="체크1")
chk1.select()
chk1.grid(row=0, column=0)
tk.Checkbutton(lbFrame2, text="체크2").grid(row=0, column=1)
tk.Checkbutton(lbFrame2, text="체크3").grid(row=0, column=2)

# 라디오버튼
colors = ['Blue','Yellow','Red']
radioColor = tk.IntVar()
for col in range(3):
    rad = tk.Radiobutton(lbFrame2, text=colors[col], variable=radioColor, value=col, command=selColor)
    rad.grid(row=1, column=col)

color = ttk.LabelFrame(lbFrame2, text=colors[0])
color.grid(row=3,column=0,columnspan=3)
ttk.Label(color, text='Label 1').grid(row=0,column=0)
ttk.Label(color, text='Label 2').grid(row=1,column=0)
ttk.Label(color, text='Label 3').grid(row=2,column=0)

win.mainloop()