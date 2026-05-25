# Ⅰ 조건문  과제 [1~5번까지 수행. 시간이 남으면 6번~12번 수행] 
# 문제1. 
# 사용자로 부터 정수 하나를 입력받아라. 입력받은 정수의 절대값을 출력하는 프로그램을 
# 작성하시오. 

user_input_integer = int( input("원하는 정수를 입력하세요:>>> "))

if user_input_integer >=0:
    print(f"{user_input_integer}의 절대값: {user_input_integer}")
else: # user_input_integer <=-1:
    print(f"{user_input_integer}의 절대값: {-user_input_integer}")

print()
