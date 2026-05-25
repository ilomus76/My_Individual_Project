

# 변수와 자료형 및 키보드 입력기능 : input() 과제 
# 문제 4. 간단한 계산기 만들기 
# 두 숫자를 변수로 저장한 뒤, 
# 덧셈, 뺄셈, 곱셈, 나눗셈 결과를 각각 출력해보세요. 
# num1 = 10 
# num2 = 3 
# 출력 예) 
# 덧셈 결과: 13 
# 뺄셈 결과: 7 
# 곱셈 결과: 30 
# 나눗셈 결과: 3.3333333333 

str = "간단한 계산기 만들기 연습"
print(str)
num1 = input("첫번째 숫자를 읿력하세요:> ")
num2 = input("두번째 숫자를 입력하세요:> ")

addition_result = int(num1) + int(num2)
substraction_result = int(num1) - int(num2)
multiplication_result = int(num1)*int(num2)
divide_result = float(int(num1))/(float(int(num2)))

print("덧셈 결과:",addition_result)
print("뺄셈 결과:",substraction_result)
print("곱셈 결과:",multiplication_result)
print("나눗셈 결과:",divide_result)

