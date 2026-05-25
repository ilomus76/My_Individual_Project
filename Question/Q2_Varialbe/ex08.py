# 변수와 자료형 및 키보드 입력기능 : input() 과제 
# 문제8. 
# 하나의 정수를 입력 받아서, 그 수의 제곱의 결과를 출력하는 프로그램을 작성해보자. 
# 예들 들어서 5가 입력되면 25가 출력되어야 한다. 

num1 = input(" 제곱을 만들기 위한 숫자 하나를 입력하세요:> ")

#num1 is string not number
# Thus, cast to change the type from string to integer is required.
temp_num1 = int(num1)

print("입력한 숫자 {}의 제곱은 {}입니다.".format(num1,temp_num1**2))