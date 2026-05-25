# Title 
#import os 
#import sys

import pandas as pd


########### Prototype area ###################

 
class score_data:
    # class variable generation
    def __init__(self,name,kor,eng,math):
        self.name = name
        self.kor = kor 
        self.eng = eng
        self.math = math 
    def score_sum(self):
        return self.kor + self.en + self.math 
        
    def score_average(self):
        return (self.kor + self.en + self.math )/3

    @classmethod
    def anyfunction(self):
        pass

#################################################

print('@'*100)
print('\t 성적 통계 프로그램')
print('@'*100)

# cSV 파일 Open
# stream definition 

# open 은 표준 함수 
#file = open('Question/Homework/scores.csv','r') 
file = open('Question/Homework/scores.csv','r',encoding='UTF-8') 
#file = open('Question/Homework/scores.csv','r',encoding='ANSI') 

print('Pandas 로 데이타 읽기')
data_frame=pd.read_csv('Question/Homework/scores.csv')
print(data_frame)
# print(data_frame.shape)
# print(data_frame.head())
# print(data_frame.tail())
# print(data_frame.columns)
# print(data_frame.columns[1])
# print(data_frame.loc[0]) # Pandas의 행/열을 이름(label) 기준으로 선택하는 기능 , 인덱스(label)가 1인 행을 가져와라 
# print('ㅅㅅㅅㅅ',data_frame.loc[0:1,'국어'])
# # print(data_frame.iloc[0][0])
# # print(data_frame['국어'][1]) # '국어' key 의 1번 : 세로방향.
# # rows = aa.loc[2:,['이름','수학']] # 2번부터 끝까지, 이름하고 수학만..



n=0
total = []
avg = []

min_=[]
max_=[]

# 2. 데이터 처리 : 각 과목(국어, 영어, 수학)에 대해 다음을 계산하시오. 
# 평균 점수 
# 최고 점수 
# 최저 점수 

for s in data_frame: # key->str.
    if n==0:
        n+=1
        continue
    else:
        n+=1
        #print(s)                               #key
        #print(s,'-평균:', sum(data_frame[s]))  # value for each key
        #print('합',list(data_frame[s]),)       
        
        #print(len(data_frame[s]))
        
        total.append(sum(data_frame[s]))
        #print(total)
        avg.append(total[n-2]/len(data_frame[s]))         
        #print(avg)

        min_.append(min(data_frame[s]))
        #print(min_)
        max_.append(max(data_frame[s]))
        #print(max_)



# 3. 결과 출력 : 각 과목별 통계 결과를 콘솔에 보기 좋게 출력하시오. 
# 예) 
# [과목별 통계] 
# 국어 - 평균: 85.5, 최고점: 92, 최저점: 76 
# 영어 - 평균: 88.0, 최고점: 94, 최저점: 80 
# 수학 - 평균: 84.0, 최고점: 95, 최저점: 72 

print('@'*100)
print('[과목별 통계]')

for d in range(len(data_frame.columns)-1):
    s= f"{data_frame.columns[d+1]}- 평균: {avg[d]}, 최고점: {max_[d]}, 최저점: {min_[d]}"
    print(s)
print('@'*100)
# print(len(data_frame[s]))        
# print(total) 
# print(avg)

# print('국어 - ','평균:', data_frame['국어'].mean(), '최고점:',data_frame['국어'].max(),'최저점:',data_frame['국어'].min())
# print('영어 - ','평균:', data_frame['영어'].mean(), '최고점:',data_frame['영어'].max(),'최저점:',data_frame['영어'].min())
# print('수학 - ','평균:', data_frame['수학'].mean(), '최고점:',data_frame['수학'].max(),'최저점:',data_frame['수학'].min())


# 4. 결과 파일로 저장 (선택 과제) 
# 각 학생의 총점과 평균도 계산하시오. 

#print(data_frame)
data_frame['총점'] = [0 for i in range(8)]  # element addition
data_frame['평균'] = [0 for i in range(8)] 

# with open('Question\Homework\ result.csv', 'w', encoding='UTF-8') as f:
#     data_frame.to_csv(f, index=False)


temp=[] 
temp2=[]
print(temp)
for s in range(0,8):  
    a=0  
    for i in range(1,4):
        #print(data_frame.loc[s,data_frame.columns[i]])          
        a += data_frame.loc[s,data_frame.columns[i]]
        #print(data_frame.loc[s,data_frame.columns[i]])
        
        #print(data_frame.loc[1,[data_frame.columns[2]]])
        #pass
        #print(data_frame.loc[0])
        #print(a)
    temp.append(int(a))
    temp2.append(round((int(a)/3),2) )
    #print('test',temp)    
    #print(type(data_frame['총점']))
# 각 학생의 이름, 총점, 평균을 포함한 새로운 CSV 파일(result.csv)로 저장하시오. 
data_frame['총점']=temp
data_frame['평균']=temp2
#print('test',temp) 
print(data_frame)
#print(data_frame['총점'])


# # 4. 결과 파일로 저장 (선택 과제) 
# # 각 학생의 총점과 평균도 계산하시오. 
# # 각 학생의 이름, 총점, 평균을 포함한 새로운 CSV 파일(result.csv)로 저장하시오. 

with open('Question\Homework\\result.csv', 'w', encoding='UTF-8',newline='') as f:
    data_frame.to_csv(f, index=False, lineterminator ='\n')
# with open('Question\Homework\ result.csv', 'w', encoding='UTF-8') as f:
#     data_frame.to_csv(f, index=False)

#data_frame.to_csv('result.csv', index=False, encoding='ANSI')



# file = open("Question\Homework\ result.csv",'w',encoding="ANSI")

# # s = ""
# # for i in range(len(each_data_line)):
# #     for n in range(len(each_data_line[i])):
# #         s += str( each_data_line[i][n]) + ','
# #     s += '\n'     

# # print(s)
# # print()
# file.write(data_frame)
# file.close()





#//////////////////////////////////////////
# 이번에는 readlines()를 사용했네요.
# 이 경우 결과가 readline() 때와 조금 다르게 나옵니다.
# 핵심 부분:
# data = file.read()
# 여기서 이미 파일 전체를 읽었습니다.
# 그래서 파일 포인터가 EOF(파일 끝)에 위치합니다.
# 그 다음:
# data1 = file.readlines()
# 를 실행하면 읽을 줄이 더 이상 없기 때문에:
# []
# 즉 빈 리스트가 반환됩니다.
# 여기서 중요한 차이:

# 함수	반환형	EOF 상태 결과
# read()	문자열(str)	''
# readline()	문자열(str)	''
# readlines()	리스트(list)	[]

# 따라서 현재 코드 출력은 대략 이렇게 됩니다.

# read_data type : <class 'str'>
# read data : (파일 전체 내용)

# read_data type : <class 'list'>
# read data : []

# 왜 리스트일까요?
# readlines()는 파일의 각 줄을 리스트 요소로 저장하기 때문입니다.
# 예를 들어 파일 내용이:
# Kim,90
# Lee,80
# Park,70
# 이면:
# file.readlines()
# 결과:
# ['Kim,90\n', 'Lee,80\n', 'Park,70']
# 입니다.
# 정상적으로 readlines()를 사용하려면:
# file.seek(0)
# data1 = file.readlines()
# 처럼 다시 처음으로 이동해야 합니다.
# 정리하면 현재 코드의 흐름은:
# file.read()       # 전체 읽기 → EOF 이동
# file.readlines()  # 더 읽을 게 없음 → []
# 입니다.
#------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------
# PYTHON 과제 
# 문제. 학생들의 성적이 저장된 scores.csv 파일을 이용한 성적 통계 프로그램을 
# 만들어보시오. 
# 과제 요구사항 
# 1. CSV 파일 읽기 : open() 함수를 사용하여 scores.csv 파일을 읽으시오. 
# [* 첫줄(헤더)을 제외한 나머지 줄의 점수를 숫자(int) 데이터로 변환해야만 
# 계산가능] 
# 2. 데이터 처리 : 각 과목(국어, 영어, 수학)에 대해 다음을 계산하시오. 
# 평균 점수 
# 최고 점수 
# 최저 점수 
# 3. 결과 출력 : 각 과목별 통계 결과를 콘솔에 보기 좋게 출력하시오. 
# 예) 
# [과목별 통계] 
# 국어 - 평균: 85.5, 최고점: 92, 최저점: 76 
# 영어 - 평균: 88.0, 최고점: 94, 최저점: 80 
# 수학 - 평균: 84.0, 최고점: 95, 최저점: 72 
# 4. 결과 파일로 저장 (선택 과제) 
# 각 학생의 총점과 평균도 계산하시오. 
# 각 학생의 이름, 총점, 평균을 포함한 새로운 CSV 파일(result.csv)로 저장하시오. 
# #solution guide 
# 평균, 최고, 최저 점수를 계산하는 것을 반복문과 연산자로 수행하는 문제이지만,(필수 아님) 
# 파이썬의 표준내장함수 중에 이 값들을 쉽게 계산해주는 기능함수가 이미 존재함.  
# 배열(리스트,튜플,딕셔너리)수업에 일부 소개되었음. 즉, 계산을 편히 하려면 읽어들인 값들을 
# 리스트로 만들면 표준함수로 문제를 해결할 수도 있음. 학습하지 않은 내용은 검색하여 수행 
# [표준함수 ex : print(), input(), len(), max(). . . ] 
# 제출해야 할 내용 
# 아래 2가지를 반드시 제출하세요 
# ① Python 소스 코드 (.py) 
# ● 하나의 파일로 제출하거나 
# ● 모듈 형태로 작성된 경우 여러 파일이 있어도 무방함. 
# ② 실행 화면 캡처 (jpg/png + csv ) 
# 다음 항목들을 준비하여 파이썬 파일과 함께 제출 합니다 
# ● 결과 출력 화면 캡처 이미지 
# ● (동작 안될경우) 실행했을때 보여지는 에러 메세지 캡처 이미지 
# ● (선택과제)저장된 파일 이름이 보이는 목록 화면(윈도우 탐색기 or VSCode Explorer) 
# 캡처 
# ● (선택과제)저장된 CSV 파일 
# 제출 방법 
# ● 교강사 공유폴더 > 교과목별 평가 > 01 PYTHON > 제출폴더 > 본인이름폴더 
#------------------------------------------------------------------------------------------