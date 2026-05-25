# Ⅱ문자열 연산자 과제 
# 문제1 
# 두 개의 문자열 변수 s1 과 s2를 사용자로부터 입력 받는다.  
# s1과 s2 연결하고, s2를 3번 반복하는 코드를 작성하세요. 
# 입력값 예) 
# s1= “Hello” 
# s2= “Python” 
# 출력 
# Hello Python 
# PythonPythonPython


s1 = input ( "문자열 입력1: ")
s2 = input ( "문자열 입력2: ")

temp_s = s1 + s2
temp_s2 = s2*3

print(temp_s)
print(temp_s2)