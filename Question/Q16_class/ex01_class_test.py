#'seoul_weather_2026.xlsx' 파일의 한줄 데이터를 저장하는 클래스 설계(변수,생성자,출력기능)해 보기. 
# 마지막 교시에 배운 내용


import os
import sys 
import pandas as pd

class FileAccess:
    file = None # 클래스 변수 
    data = ''

    def __init__(self,file_name): # 초기화함수(생성자 함수)
        #self.file_name = file_name

        pdata=pd.read_excel(file_name)
        #print(pdata)
        #print(type(pdata))

        #print(pdata.columns)       
        print(pdata.loc[0])
        #print(pdata.describe())
        # FileAccess.file = open(file_name,'r',encoding='UTF-8')
        # FileAccess.data = FileAccess.file.readlines()
        # FileAccess.file.close()

     
FileAccess('Question/Q16_class/seoul_weather_2026.xlsx')
        


