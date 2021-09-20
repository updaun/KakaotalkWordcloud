from wordcloud import WordCloud
import konlpy
import numpy as np
import pandas as pd
import re
import matplotlib.pyplot as plt
plt.rc('font', family='NanumBarunGothic')     # 한글 깨짐 방지
from PIL import Image                         # Pillow 패키지의 영상 핸들링 클래스
import os                                     # 파일 확인
# import natsort                                # 파일 정렬

def make_wordcloud(input_path):
    PATH = input_path      
    image_PATH = "./masks/background_3.png"       

    no_meaning_list = ''         # 불용어 추가하기 (없으면 그대로 둘 것) * 예시 : '안녕' '안녕|잘가'  '안녕|잘가|잘자'
    word_length = 1              # 단음절 수 삭제 기준 (변경 가능)

    words_num = 100               # 워드클라우드 표시 단어 수

    # 파일명 가져오기

    # file_list = os.listdir(PATH)
    # text_list = list()

    # for file in file_list:
    #     if file.split(".")[-1] == 'txt':  # check
    #         text_list.append(file)

    # text_list = natsort.natsorted(text_list) # natsort 정렬



    # 카카오톡 데이터 불러오기

    # text_list_all = []

    # for i in text_list :
    #    with open(PATH+i, 'r', encoding='utf-8-sig') as f :
    #       my_text = f.readlines()
    #       text_list_all.extend(my_text)  # extend    

    text_list_all = []

    with open(PATH, 'r', encoding='utf-8-sig') as f :
        my_text = f.readlines()
        text_list_all.extend(my_text)  # extend    

    # 기본 불용어
    no_meaning = 'ㅠ|ㅜ|ㅡ|ㅋ|ㅎ|' 
    no_meaning += '이모티콘|사진'

    # 불용어 추가
    if len(no_meaning_list) > 1 :
        no_meaning += "|" + str(no_meaning_list)


    # 텍스트 부분 발췌
    my_line = [ a_line.split(':') for a_line in text_list_all]

    my_line_word = []

    for a_line in my_line :

        try :
            a_line = a_line[2] 

        except : 
            continue            # try - except

        my_line_word.append(a_line)     

    # 전처리
    my_line_clean = []

    for a_line in my_line_word :

        a_line = re.sub(no_meaning, ' ', a_line)     # 특별한 의미 없는 단어 스페이스로 대체.
        a_line = re.sub('\W+',' ', a_line)           # 특수 문자 스페이스로 대체.
        a_line = re.sub('[-!?()>~.,]',' ',a_line)    # 특수문자 스페이스로 대체.
        a_line = re.sub('\d+',' ', a_line)           # 숫자 스페이스로 대체.
    
        a_line = re.sub('\n',' ',a_line)             # line return 스페이스로 대체.
        a_line = re.sub('[\[\]]', ' ',a_line)        # 대괄호 스페이스로 대체.
        a_line = re.sub('[a-zA-Z]',' ',a_line)       # 영문 스페이스로 대체.
        a_line = re.sub('\s+', ' ', a_line)          # 잉여 스페이즈 줄임.

        my_line_clean.append(a_line)

    # 명사 추출
    my_tagger = konlpy.tag.Okt()

    my_words = []
    for a_line in my_line_clean:
        my_words.extend(my_tagger.nouns(a_line))  # 명사 # extend

    # 단음절 제거 
    my_words_2 = [a_word  for a_word in my_words if len(a_word) > word_length]

    # Series 로 변환
    my_series = pd.Series(my_words_2)
    my_word_counts = my_series.value_counts().sort_values(ascending=False)

    # 딕셔너리로 변환
    my_dict = {}
    for an_index, a_value in zip(my_word_counts.index,my_word_counts.values):
        my_dict[an_index] = a_value

    try : 
        img = Image.open(image_PATH)        # 이미지 있을 경우 경로 입력
        back_mask = np.array(img)           # 넘파이 배열로 변환

        wc = WordCloud(font_path='./fonts/NanumBarunpenR.otf',background_color='white', max_words= words_num, mask=back_mask, colormap='spring')           
        wc.generate_from_frequencies(my_dict)

    except :

        wc = WordCloud(font_path='./fonts/NanumBarunpenR.otf',background_color='white', max_words = words_num, colormap='spring')         
        wc.generate_from_frequencies(my_dict)


    plt.figure(figsize=(10,10))
    plt.imshow(wc)
    plt.axis("off")      
    plt.show()