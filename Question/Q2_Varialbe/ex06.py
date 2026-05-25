
# 변수와 자료형 및 키보드 입력기능 : input() 과제 
# 키보드 입력 : input()  과제 
# 문제6. 
# 프로그램 사용자로부터 두개의 정수를 입력받아서 두 수의 뺄셈 과 곱셈의 결과를 
# 출력하는 프로그램을 작성해 보자. 

print("이 프로그램은 사용자로부터 두개의 정수를 입력받아서 두 수의 뺄셈과 곱셈을 보여줄 것입니다.")
print("두수를 차례대로 입력하세요.")
print()
num1 = input(" 첫번째 숫자를 입력하세요: ")
num2 = input(" 두번째 숫자를 입력하세요: ")

num1_cast = int(num1)
num2_cast = int(num2)

substraction_num1_num2 = num1_cast - num2_cast 
addition_num1_num2     = num1_cast + num2_cast 

print("두수의 뺄셈의 결과는 {}입니다".format(substraction_num1_num2))
print("두수의 덧셈의 결과는 {}입니다".format(addition_num1_num2))