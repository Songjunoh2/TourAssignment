from tkinter import * #tkinter 임포트
import os

def openUrl(url):
    webbrowser.open_new(url)

mainWindow = Tk()                           #메인화면 창
mainWindow.geometry("450x800")              #창의 해상도
mainWindow.title("전라북도 관광 홍보 프로그램")    #창 제목

titleJeonju = Button(mainWindow, 
                    text="전주", 
                    font=("", "20"), 
                    pady=("10"),
                    openUrl=("https://tour.jb.go.kr/index.do?menuCd=DOM_000000102001001001")) # 전주 버튼
                    
titleJeonju.pack() # 전주 버튼 배치

jeonju=PhotoImage(file='/Users/imseokjun/Desktop/Github/TourAssignment/Code/img/jeonju.png')
# 파일 이미지 불러오기 (사진 절대경로임. 수정해야함.)

jeonjuImage=Label(mainWindow, image=jeonju)
jeonjuImage.pack() # 이미지 배치


mainWindow.mainloop()
