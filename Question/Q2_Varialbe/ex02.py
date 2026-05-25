# 변수와 자료형 및 키보드 입력기능 : input() 과제 
# 문제 2. 변수로 문장 만들기 
# 이름, 나이, 취미를 변수로 저장한 후, print()로 다음과 같이 출력해보세요. 
# [hint: + 또는 , 로 문자열 연결 가능, or format(), f-string ] 
# 제 이름은 [이름]이고, 나이는 [나이]살입니다. 
# 제 취미는 [취미]입니다. 
# 출력 예) 
# 제 이름은 홍길동이고, 나이는 25살입니다. 
# 제 취미는 수영, 달리기 입니다. 

name = input("이름을 입력하세요: ")
age = input("당신의 나이를 입력하세요: ")
hobby = input("당신의 취미를 입력하세요: ")

print("제 이름은 {}이고, 나이는 {} 살입니다.".format(name,age))
print("제 취미는 {}입니다.".format(hobby))
print()
print(f"제 이름은 {name}이고, 나이는 {age} 살입니다.")
print(f"제 취미는 {hobby}입니다.")
print()
print("제 이름은",name,"이고, 나이는",age,"살입니다.")
print("제 취미는",hobby,"입니다.")
print()