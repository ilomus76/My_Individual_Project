# 문제 3. 
# 아래와 같이 학생들의 성적을 받아서 score_list 라는 이름의 리스트에 저장하고, 
# 평균을 구하는 프로그램을 작성해보자. (평균은 소수점 2자리까지만 표시) 
# 단, 입력값이 0~100 사이가 아니면 다시입력하도록 하시오.  
# 실행결과 예시) 
# 학생의 수를 입력하시오 : 2 
# 학생 1의 성적을 입력하세요 : 20 
# 학생 2의 성적을 입력하세요 : 110 
# 잘못된 성적입니다. 다시 입력하시오. 
# 학생 2의 성적을 입력하세요 : 30 
# —-------------------- 
# 학생 1의 성적 : 20 
# 학생 2의 성적 : 30 
# —-------------------- 
# 성적 평균은 25.00 입니다. 

student_numbers = int ( input('학생의 수를 입력하시오 : >>>> '))
student_score_list=[]

for e in range(student_numbers):
    s="학생 {:d}의 성적을 입력하세요".format(e+1)
    temp = int( input(s))
    if 0< temp <100:
        student_score_list.append(temp)
    else:
        print("잘못된 성적입니다. 다시 입력하시오.:")
        temp = int(input(s ))
        student_score_list.append(temp)

total = 0
for e in range(student_numbers):
    total += student_score_list[e]

print("성적 총합은 ",total/student_numbers)  
