# 변수와 자료형 및 키보드 입력기능 : input() 과제 


# 문제 3. 자료형 확인하기 
# 다음 변수를 만들고, 각각의 자료형을 출력해보세요. 
# name = "철수" 
# age = 15 
# height = 165.3 
# is_student = True 
# 출력 예) 
# <class 'str'> 
# <class 'int'> 
# <class 'float'> 
# <class 'bool'> 


name = input("당신의 이름을 입력하세요:")
age = input("당신의 나이를 입력하세요: ")
height = input("당신의 키를 입력하세요: ")
is_student = input("당신은 학생인가요?: 맞으면 True 아니면 False를 입력하세요: ")
print()
print(name, type(name))
print(int(age),type(int(age)))
print(float(height),type(float(height)))
print(bool(is_student),type(bool(is_student)))

