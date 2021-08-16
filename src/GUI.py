from tkinter import *
import tkinter.font
from wordcloud_download import Downloader
from tkinter import messagebox
from tkinter import filedialog

path = ''

# file explorer window
def browseFiles():
    global path
    path = filedialog.askopenfilename(initialdir="/", title="대화내용 파일 선택",
                    filetypes=(("txt files", "*.txt"),("all files", "*.*")))
    
    print("[파일 선택] :", path,'\n')
    # Change label contents
    label_file_explorer.configure(text="File Opened: "+ path)




dl = Downloader()

projectTitle = 'Kakaotalk Wordcloud v1.0'

# 사용 색상
bgcolor = '#FFE812' 
btncolor = '#2E2E30' 

# 창 생성
root = Tk()
# 프로그램 크기 및 위치 지정
root.geometry("440x450+500+150")
#프로그램 창 크기 변경 제한
root.resizable(False, False)
# 프로그램 상단 타이틀 바 로고 import
root.iconphoto(False, PhotoImage(file='.\image\kakaotalk.png'))
# 프로그램 배경 설정
root.configure(bg=bgcolor)
# 프로그램 상단 타이틀 바 명칭 설정
root.title("카카오톡 워드클라우드")

# 폰트 설정
font = tkinter.font.Font(family="KoPubWorld돋움체 Medium",
                         size=15, weight=tkinter.font.BOLD)  # 버튼 폰트
font0 = tkinter.font.Font(family="KoPubWorld돋움체 Medium", size=1)  # 공백 폰트
font1 = tkinter.font.Font(family="KoPubWorld돋움체 Medium", size=11)  # 설명 폰트
font2 = tkinter.font.Font(family="KoPubWorld돋움체 Medium", size=18)  # TEXT 박스
font25 = tkinter.font.Font(family="KoPubWorld돋움체 Medium", size=25)  # 공백 폰트
font3 = tkinter.font.Font(family="KoPubWorld돋움체 Medium",
                          size=18, weight=tkinter.font.BOLD)  # Title 폰트
# 메인 로고 import
image1 = PhotoImage(file=".\image\kakaotalk.png")
# 로고 사이즈 조절
photoimage1 = image1.subsample(8, 8)
# 로고를 라벨로 설정
imgLabel1 = Label(root, image=photoimage1, width=85,
                  height=85, background=bgcolor)

# Create a File Explorer label
label_file_explorer = Label(root,
                            text = "File Explorer using Tkinter",
                            width = 100, height =4,
                            fg = "blue")
# 버튼 설정
btn_1 = Button(root, text="대화내용 업로드", width=20, height=1, font=font,
                        foreground='white', background=btncolor, command = browseFiles)
  
btn_2 = Button(root, text="대화내용 분석", width=20, height=1, font=font,
            foreground='white', background=btncolor, command=lambda: dl.action(path))

# 공백 설정
label000 = Label(root, text='', anchor="sw", width=40,
                 height=1, font=font25, background=bgcolor)
label001 = Label(root, text='', anchor="sw", width=40,
                 height=1, font=font0, background=bgcolor)
label002 = Label(root, text='', anchor="sw", width=40,
                 height=1, font=font0, background=bgcolor)
label003 = Label(root, text='', anchor="sw", width=40,
                 height=1, font=font0, background=bgcolor)

# 프로그램명 설정
systemTitle = Label(root, text=projectTitle, anchor="center",
                    width=40, height=1, font=font3, background=bgcolor, fg='#2f3640')
# 설명 입력
label2 = Label(root, text='[업로드] Kakaotalk 대화내용을 넣어주세요.', anchor="sw",
               width=30, height=1, font=font1, background=bgcolor, padx=80)

# 설명 입력
label3 = Label(root, text='[분석] WordCloud로 대화내용을 분석합니다.', anchor="sw",
               width=30, height=1, font=font1, background=bgcolor, padx=80)
# 텍스트 박스 설정
# inputText = Entry(root, width=35, font=font1,
#                   background='azure', relief='solid')

# 공백
label000.pack()
# 메인로고
imgLabel1.pack()
# 공백
label001.pack()
# 프로그램명
systemTitle.pack()
# 공백
label002.pack()
# 설명_2
label2.pack()
# 텍스트 박스

# 버튼_1
btn_1.pack()

# inputText.pack()
# 공백
label003.pack()

# 설명_3
label3.pack()

# 버튼_2
btn_2.pack()

# 'Enter' 키를 눌러 '동영상 다운로드' 버튼 클릭
# root.bind('<Return>', lambda event=None: btn.invoke())
  
root.mainloop()