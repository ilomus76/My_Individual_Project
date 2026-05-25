# 학생 리스트를 선업합니다.

# Dictionary 변수를 요소로 하는 리스트 작성.
students = [ 
    {'name':'윤인성','korean':87,'math':98, "english":88, "science":95}, 
    {'name':'연하진','korean':92,'math':98, "english":96, "science":98},
    {'name':'구지연','korean':76,'math':96, "english":94, "science":90},
    {'name':'나선주','korean':98,'math':92, "english":96, "science":92},
    {'name':'윤아린','korean':95,'math':98, "english":98, "science":98},
    {'name':'윤명월','korean':64,'math':88, "english":92, "science":92}
            ]
# 학생을 한 명씩 반복합니다.
#print('이름','총점','평균')
print('이름','총점','평균',sep='\t')


for student in students:   # iterator 로 사용 
    # 점수의 총합과 평균을 구합니다.
    score_sum = student['korean'] + student['math'] + \
        student['english'] + student['science']   
    score_average = score_sum / 4 

    # 출력합니다.
    print(student['name'], score_sum, score_average, sep='\t')