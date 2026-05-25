# 클래스를 선언합니다.
class Student:
    def __init__(self,name, korean,math,english,science): # 초기화 함수 
        #멤버 변수, 인스턴스 변수 선언 및 초기화 => self라는 자기의 변수임을 지시를 꼭 해 줘야 한다. 
        self.name = name  
        self.korean = korean
        self.math = math
        self.english = english
        self.science =science
    def get_sum(self):
        return self.korean + self.math + self.english + self.science 

    def get_average(self):
        return self.get_sum()/4

    def to_string(self):
        return "{}\t{}\t{}".format(self.name,self.get_sum(),self.get_average())

# 학생 리스트를 선언합니다.
students = [ 
    Student('윤인성',87,98,88,95),    # 변수에 생성자를 대입하면서 객체를 만드는 형태임... 
    Student('연하진',92,98,96,98), 
    Student('구지연',76,96,94,92), 
    Student('나선주',98,92,96,98), 
    Student('윤아린',95,98,98,98), 
    Student('윤명월',64,88,92,92), 
            ]

# 학생을 한 명씩 반복합니다.
print('이름','총점','평균',sep='\t')
for student in students:
    #출력합니다. 
    print(student.to_string()) 


# 이름    총점    평균
# 윤인성  368     92.0
# 연하진  384     96.0
# 구지연  358     89.5
# 나선주  384     96.0
# 윤아린  389     97.25
# 윤명월  336     84.0
        