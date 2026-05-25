# 클래스를 선언합니다.
class Student:
    # 클래스 변수 
    count = 0 
    students = [] 

    # 클래스 함수 
    @classmethod
    def print(self):
    #def print(cls):
        print('------학생 목록 -------')
        print('이름\t총점\t\평균')
        for student in self.students:
            print(str(student))
        print("-------------------")
    # 인스턴스 함수
    def __init__(self,name, korean,math, english, science):
        self.name = name 
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
        Student.count +=1
        Student.students.append(self)

    def get_sum(self):
        return self.korean +self.math + self.english + self.science

    def get_average(self):
        return self.get_sum()/4

    def __str__(self):
        return "{}\t{}\t{}".format(self.name, self.get_sum(), self.get_average())

#학생 리스트를 선언합니다.

Student('윤인성',87,98,88,95)    # 변수에 생성자를 대입하면서 객체를 만드는 형태임... 
Student('연하진',92,98,96,98) 
Student('구지연',76,96,94,92) 
Student('나선주',98,92,96,98) 
Student('윤아린',95,98,98,98) 
Student('윤명월',64,88,92,92) 


#현재 생성된 학생을 모두 철력합니다.
Student.print()
