# Tkinter 주요 위젯

# Button        버튼
# Label         텍스트 또는 이미지 표시
# CheckButton   체크박스
# Entry         단순한 라인 텍스트 박스 (html의 input태그 기능)
# ListBox       리스트 박스
# RadioButton   옵션 버튼
# Message       Label과 비슷하게 텍스트 표시, Label과 다르게 자동 래핑 가능
# Scale         슬라이스바 (트랙바 기능)
# Scrollbar     스크롤바
# Text          멀티라인을 제공하는 텍스트박스
# Menu          메뉴
# Menubutton    메뉴 버튼
# Toplevel      새로운 윈도우를 생성할 때 사용. Tk()는 윈도우를 자동으로 생성하는 클래스이다. 
#               여기에 추가로 새로운 윈도우를 또는 다이얼로그를 만들 경우에 Toplevel을 사용한다.
# Combobox      드롭다운 콤보 상자
# Frame         컨테이너 위제. 다른 위젯들을 그룹핑할 때 사용한다.
# Canvas        그래프와 점들로 그림을 그릴 수 있는 위젯, 커스텀 위젯을 만들 때 사용한다.

import tkinter as tk

# 인스턴스 생성
win = tk.Tk()

# 윈도우의 사이즈 조정 차단
win.resizable(0,0) # -> 창크기조정이 안된다.
win.resizable(1,0) # -> 세로 조정이 안된다. 가로만 가능
win.resizable(0,1) # -> 가로 조정이 안된다. 세로만 가능

win.title("파이썬 GUI")

# 이벤트가 전달되기를 기다리는 무한루프
win.mainloop()