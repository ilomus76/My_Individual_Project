# 딕셔너리를 리턴하는 함수를 선언한다.
def create_student(name, korean,math,english,science):
    return {
        "name":name,
        "korean":korean,
        "math" : math,
        "english" : english,
        "science" : science
    }

# 학생 리스트를 선언합니다. 
# 함수 호출로 딕셔너리 요소를 만들어 갖게 됨. 
students = [ 
    create_student('윤인성',87,98,88,95), 
    create_student('연하진',92,98,96,98), 
    create_student('구지연',76,96,94,92), 
    create_student('나선주',98,92,96,98), 
    create_student('윤아린',95,98,98,98), 
    create_student('윤명월',64,88,92,92), 
            ]

#학생을 한명씩 반복합니다.
print('이름','총점','평균',sep='\t')

for student in students:
    #점수의 총합과 평균을 구합니다.
    score_sum = student['korean'] + student['math'] + \
        student['english'] + student['science']
    score_average = score_sum / 4 

    #출력합니다.
    print( student['name'], score_sum, score_average,sep='\t')
    