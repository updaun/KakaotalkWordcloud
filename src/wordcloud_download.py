import os
from tkinter import messagebox
import sys
from wordcloud_modules import make_wordcloud

class Downloader:
        
    def action(self, path):
        if path == '':
            print('[오류] 대화내용 파일을 선택해주세요.\n')
            messagebox.showwarning("카카오톡 워드클라우드", "대화내용 파일을 선택해주세요.")

        else:
            self.path = path
            # download_path = './Downloads'
            dl = Downloader()
            # 폴더 생성 함수 호출
            # dl.createFolder(download_path)
            # 유튜브 동영상 다운로드 함수 호출
            dl.wordcloud_download(self.path)


    # 다운로드 폴더 생성 함수
    # def createFolder(self, directory):
    #     try:
    #         if not os.path.exists(directory):
    #             # 폴더 생성 메서드
    #             os.makedirs(directory)
    #     except Exception as all_e: 
    #         # 에러 발생시
    #         print('[오류] 폴더 생성을 실패하였습니다.\n' + directory)
    #         print('[에러코드]', type(all_e))
    #         print('[에러내용]', all_e,"\n")
    #         messagebox.showwarning("카카오톡 워드클라우드", "[오류] 폴더 생성을 실패하였습니다.")



    # 유튜브 동영상 다운로드 함수 
    def wordcloud_download(self, textfile_path):
        # def show_progress_bar(stream, _chunk, bytes_remaining):
        #     current = ((stream.filesize - bytes_remaining)/stream.filesize)
        #     percent = ('{0:.1f}').format(current*100)
        #     progress = int(50*current)
        #     status = '█' * progress + '-' * (50 - progress)
        #     sys.stdout.write(' ↳ |{bar}| {percent}%\r'.format(bar=status, percent=percent))
        #     sys.stdout.flush()

        print('[진행] 대화내용 분석을 시작합니다.\n')

        
        try:
            make_wordcloud(textfile_path)
        
        except Exception as all_e:
            pass
            # print('[오류] 대화내용 파일을 다시 확인해 주세요.\n')
            # print('[에러코드]', type(all_e))
            # print('[에러내용]', all_e,"\n")
            # messagebox.showinfo(
            # "카카오톡 워드클라우드", "[오류] 링크 주소를 다시 확인해 주세요.")


        # print('[완료] 대화내용이 분석 되었습니다.\n')
        # messagebox.showinfo(
        # "카카오톡 워드클라우드", "대화내용이 분석 되었습니다.")

########################################################################################
# test code
########################################################################################

# with open('./src/test_url.txt', 'r') as file_data:
#     for line in file_data:
#         print(line)
#         test_url = line
        
# dl = Downloader()
# dl.youtube_download(test_url)