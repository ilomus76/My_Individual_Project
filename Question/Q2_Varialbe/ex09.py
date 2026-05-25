
# 변수와 자료형 및 키보드 입력기능 : input() 과제 
# 문제9. 
# 프로그램 사용자로부터 두 개의 실수를 입력 받아서 2개의 변수를 저장하자. 
# 그리고 두 변수의 사칙연산 결과를 출력해보자. 

num1 = input("첫번째 실수를 입력하세요: ")
num2 = input("두번째 실수를 입력하세요: ")

float_cast_num1 = float(num1)
float_cast_num2 = float(num2)


add = float_cast_num1 + float_cast_num2
sub = float_cast_num1 - float_cast_num2
mul = float_cast_num1 * float_cast_num2
div = float_cast_num1 / float_cast_num2 

print(" 두수 {},{}의 덧셈은 {}입니다.".format(float_cast_num1,float_cast_num2,add))
print(" 두수 {},{}의 뺄셈은 {}입니다.".format(float_cast_num1,float_cast_num2,sub))
print(" 두수 {},{}의 곱셈은 {}입니다.".format(float_cast_num1,float_cast_num2,mul))
print(" 두수 {},{}의 곱셈은 {}입니다.".format(float_cast_num1,float_cast_num2,div))

