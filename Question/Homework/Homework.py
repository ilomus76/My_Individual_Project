import sys


print('[과목별 통계]')

# 1. CSV 파일 읽기 : open() 함수를 사용하여 scores.csv 파일을 읽으시오.
print(sys.stdout.encoding)
print(type(sys.stdout.encoding)) 

s = sys.stdout.encoding
encoding_type_str = 'ANSI' if(s == 'ANSI') or (s=='cp949') or (s=='cp1252') else 'UTF-8'

with open('Question/Homework/scores.csv','r',encoding=encoding_type_str) as file:
    # Ask AI a question about how to distinguish the encoding type on the computure system. 
    # Go to www.google.com and then type chat GPT on the search line to enter into Chat GPT.
    # My question to AI 
    # Python프로그램에서 file을 열려고 하는데 나의 시스템이 ANSI를 사용하는지 UTF-8을 사용하는지를 판별하는 방법을 알려주세요.
    # Answer : https://use.ai/ko/d43615ac-2bd8-4826-a07d-a8895545e059
    # sys.stdout.encoding 확인 (콘솔 인코딩)
    # 현재 출력 환경(터미널, 콘솔)의 인코딩을 알려줍니다.
    #---------------------------------------------------------------------
    # import sys
    # print(sys.stdout.encoding)
    # 만약 콘솔창이 UTF-8을 지원한다면 "UTF-8"이 나오고,
    # Windows CMD 기본값이면 "cp949" 또는 "cp1252" 등으로 나타납니다.
    # ---------------------------------------------------------------------


    
    data = file.read() # read data from file  
    print(type(data)) # data type is <class 'str'>
    # The data is still the bundle of data. 
    # we need to seperate the data into each catagory.
    print(data) # 
    print('data size:',len(data)) # 
    data2 = data.strip().split('\n')
    print(data2) #
    print(type(data2)) # <class 'list'>
    print(len(data2))
    data3=data2.split(',')
    print(data3)

    # grade_score_dict = {} # blank dictionary
    # grade_score_dict[data2[0][1]]=0
    # grade_score_dict[data2[0][2]]=0
    # grade_score_dict[data2[0][3]]=0
    
    print(grade_score_dict)
     
    # for n in range(1,len(data2)):
    #     grade_score_dict[data2[0][1]] += grade_score_dict[data2[n][1]] # 국어
    #     # grade_score_dict[data2[0][2]] += grade_score_dict[data2[n][2]] # 영어
    #     # grade_score_dict[data2[0][3]] += grade_score_dict[data2[n][3]] # 수학
    # print(type(grade_score_dict))
    # # korean_score_avg =  grade_score_dict[data2[0][1]] / len(data2)
    # # english_score_avg =  grade_score_dict[data2[0][2]] / len(data2)
    # math_score_ave = grade_score_dict[data2[0][2]] / len(data2)
    #print('{:s} - 평균 : {:.1f}, 최고점: {:3d}, 최저점: {:3d}'.format(grade_score_dict[data2[0][1]],)

# [과목별 통계] 
# 국어 - 평균: 85.5, 최고점: 92, 최저점: 76 
# 영어 - 평균: 88.0, 최고점: 94, 최저점: 80 
# 수학 - 평균: 84.0, 최고점: 95, 최저점: 72 

    # line_count=0
    # for line_data_of_csv in file:
    #     line_count +=1
    #     if line_data_of_csv[-1]=='\n':
    #         print('개행문자가 포함된 데이타 입니다.')
    #     line_data_of_csv = line_data_of_csv #+ '\n'
    #     print('line number : {} , line text :{}'.format(line_count,line_data_of_csv))

    # print('type :',type(file))
    # print('data :',type(list(file))) 
    

    # for n in range(len(file)):
    #     for data_line in file:
    #         if n==0: # headline with each title 
    #             pass
    #         else:

    # data_line in file:






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