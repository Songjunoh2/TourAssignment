from tkinter import * #tkinter 임포트
import webbrowser

def openUrl(url):               #링크 여는 함수
    webbrowser.open_new(url)


mainWindow = Tk()                           #메인화면 창
mainWindow.geometry("450x800")              #창의 해상도
mainWindow.title("전라북도 관광 홍보 프로그램")    #창 제목

titleJeonju = Label(mainWindow, # 전주 라벨
                    text="전주", 
                    font=("궁서", "20"), 
                    pady=("10"))

titleJeonju.pack() # 전주 버튼 배치

jeonju=PhotoImage(file="./img/jeonju.png")
# 파일 이미지 불러오기

jeonjuImage=Label(mainWindow, image=jeonju)
jeonjuImage.pack() # 이미지 배치
jeonjuImage.bind("<Button-1>", lambda e: openUrl("https://tour.jb.go.kr/index.do?menuCd=DOM_000000102001001001")) # 전주 밑 이미지 클릭시 링크로 이동

mainWindow.mainloop()
