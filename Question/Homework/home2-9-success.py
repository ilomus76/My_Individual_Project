import sys
import os
import pandas as pd



print('@'*100)
print('\t 성적 통계 프로그램')
print('@'*100)

# 전역변수 영역 
data = None 
read_line_data = None
line_sorted_data= []

class StudentScore:
    total = None # 클래스 멤버 

    def __init__(self,subject_a,subject_b): # 객체가 생성되면서 바로 시작되는 초기화(객체생성자)함수
        self.subject_a = subject_a
        self.subject_b = subject_b
        self.subject_c = subject_c 

    def data_sum(self):
        total = self.subject_a + self.subject_b + self.subject_c
        return total 


    def average_calc(self):
        return round((self.subject_a + self.subject_b + self.subject_c )/3 , 2) 

# Requrement #1. CSV 파일 읽기 : open() 함수를 사용하여 scores.csv 파일을 읽으시오. 

# data를 file open으로 읽는 방법
with open('Question/Homework/scores.csv','r',encoding="UTF-8") as file:
     
    file.seek(0)
    data = file.readlines()
    # file.close()는 with 로는 안해도 된다.

    print(type(data)) # data tyie is list
    print(data)


    # [* 첫줄(헤더)을 제외한 나머지 줄의 점수를 숫자(int) 데이터로 변환해야만 
    # 계산가능]
    for i in range(len(data)):
        line_sorted_data.append(data[i].replace('\n','').split(','))
    print(line_sorted_data)
        
    for i in range(1,len(line_sorted_data)):
        for n in range(1,len(line_sorted_data[i])):
            line_sorted_data[i][n]  = int(line_sorted_data[i][n])
    print(line_sorted_data)

    # 2. 데이터 처리 : 각 과목(국어, 영어, 수학)에 대해 다음을 계산하시오. 
    # 평균 점수 
    # 최고 점수 
    # 최저 점수 
    
    total =0
    score=[0,0,0,0,0,0,0,0,0]
    temp=0
    highest=0
    lowest =100 
    
    for i in range(1,4):
        for n in range(1,len(line_sorted_data)):            
            total += line_sorted_data[n][i]
            if highest < line_sorted_data[n][i]:
                highest = line_sorted_data[n][i]
            if lowest > line_sorted_data[n][i]:
                lowest = line_sorted_data[n][i]

        score[3*i-3]   =   total
        score[3*i-2]   =   highest
        score[3*i-1]   =   lowest 
        total  =0
        lowest =100
        highest=0 
    
# korean_text  = f"국어 - 평균:{round(score[0]/(8),2)} 최고점:{score[1] } 최저점:{score[2]}"
# english_text = f"영어 - 평균:{round(score[3]/(8),2)} 최고점:{score[4] } 최저점:{score[5]}"
# math_text    = f"수학 - 평균:{round(score[6]/(8),2)} 최고점:{score[7] } 최저점:{score[8]}"
print(f"국어 - 평균:{round(score[0]/(8),2)} 최고점:{score[1] } 최저점:{score[2]}")
print(f"영어 - 평균:{round(score[3]/(8),2)} 최고점:{score[4] } 최저점:{score[5]}")
print(f"수학 - 평균:{round(score[6]/(8),2)} 최고점:{score[7] } 최저점:{score[8]}")


# 4. 결과 파일로 저장 (선택 과제) 
# 각 학생의 총점과 평균도 계산하시오. 
# 각 학생의 이름, 총점, 평균을 포함한 새로운 CSV 파일(result.csv)로 저장하시오. 



# print(type(line_sorted_data[1][1:4]))
# print(line_sorted_data[1][1:4])
# print(sum(line_sorted_data[1][1:4]))

result =['이름','총점','평균']
for i in range(1,len(line_sorted_data)):
    result.append(line_sorted_data[i][0])
    result.append(sum(line_sorted_data[i][1:3]))
    result.append(round(sum(line_sorted_data[i][1:3])/3))
   
print(result)


s = ""
for i in range(len(result)):
    if i%3 ==2:   
        s +=str( result[i]) + '\n'     
    #    s += str( result[i]) + '\n'
        #s.rstrip(',') +'\n'
    else:
        s += str( result[i]) + ','    
    
            
with open("Question/Homework/result.csv",'w',encoding='UTF-8') as file:
     file.writelines(str(s))









   


    








# data를 pandas를 통해서 읽는 방법 
# read_table_format_data = pd.read_csv('Question/Homework/scores.csv')
# print(read_table_format_data)







