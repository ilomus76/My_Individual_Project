# My python lanuuage test program
#This file is saved to HDD in the file input/output format and then loaded to
# the RAM and then excuted line by line
# To increase the capability of python programing, at least we need to try to
# create more than 500 python code
import keyword

print(" IDLE 에서 파이썬 코드를 " )
print(" 작성해서 출력해 보는")
print(" 예제입니다. " )

# 이 print 함수는 문자(열)을 모니터에 출력해 주는 함수이다.
# 이 print 함수없이 인터프리터쉘(대화형쉘)에 보여주는 것은 출력이 아니라 단순히 보여주는 것이다.
# 인터프리터 쉘(대화형쉘)에서 일반 변수나 문자열이 바로 보이지만 이것은 출력이 아닌 보여주는 기능이고
# 이것을 파일로 만들고 실행하면 일반 변수나 물자열은 print 없이 보여주지는 않는다.
# print 기능은 사용하면 개행역할까지 한다.
print()   # 이 함수는 문자(열)을 모니터에 출력해 주는 함수이다.

print("Hellow coding Python")

# "C"나 "Java"와 같이 코드가 끝나면 ;(세미콜론)으로 끝나지만 파이썬에서는 마무리 기호가 없다. 


# 표현식 : 어떠한 값을 만들어 내는 간단한 코드 
# 파이썬에서는 대소문자를 구분함. 
273 # 숫자
10 + 20   #연산자  , +,- 는 단독 그자체만으로 어떠한 값도 만들어 낼수 없기 때문에 표현식이 아님. 
"Python Programming"  # 문자열 -> 한문자의 경우는 ASCII (American standard code ? )
False # 논리값
True  # 논리값 


# Keyword 인지 확인하는 방법
print(keyword.kwlist)

# 식별자 identifier
# name_version : _ 로 표시하는 방법을 스네이크케이스(SnakeCase) , 소문자로 시작한 식별자도 스네이크케이스라고 함. 
# 함수 , 변수 , 
# NameVersion  : 첫자를 대문자로 사용하는 방법을 카멀케이스(CamelCase: 쌍봉표시법)
# 카멜케이스로 시작하면 클래스 혹은 생성자.

# 주석
# 연산자 : 이 연산은 CPU에서 하는 기능 , CPU는 연산 ( + - * /)의 기능을 수행
# CPU는 + 누산기를 이용하여 *, /, - 를 수행
# -의 경우 감산기를 보수의 기능으로 수행 ( 10의 보수(10의 반대수) 예 -2는 10-2 = 8 , 
# 7-5 = 7 + ( 10-5) = 12 , 여기서 자리올림은 버림. 그래서 결과는 2
#  9의 보수 7-5 = 7 + ( 9-5) = 11 , 이 경우 첫자리 1과 두번째 자리 1을 더함. 그래서 결국 2
#  1의 보수 1-> 0 0 ->1
#  2의 보수 1의 보수에 1을 더함. 
# 
# +의 경우 항이 두개가 오는 이항 연산자임. 
#   
# 자료 (literal : 문자그대로의) : 
# 내 생각으로는 모든 자료형을 리트럴이라고 이야기 하는 것은 있는 그대로 표현하게 되는 자료이기 때문인듯.

# 하나만 출력
print(273) # 정수 : integer , 정수는 컴퓨터에서 4바이트로 할당 
print("String") # 문자 str
print(3.14)   # 실수 float 3.14 , 실수는 컴퓨터에서 기본적으로 8byte 를 할당 이것은 double , float은 4byte 
print(3+4)

# 여러개 출력 
print(92,100,"hello")
print("안녕하세요","저희","이름은","홍길동입니다.") # print 안의 , 는 다음의 문자를 한칸 띄워 표시한다. 
print() # print()는 빈칸을 출력하기 때문에 줄바꿈(개행)으로 표시한다. 



 
#exit

##################################################################
# Commnet

# ctrl + S : save the file
# Run Module means to run/execute the python code.
# clear : remove/clean the screen
# show the itme at the current directory
#  Windows cmd or powershell: dir
#  Linux terminal           : ls
#                           : Get-Childitem
# 탐색기 explorer open 하는 방법 : explorer . 
# cd : change directory , cd directory_name , cd "directory name"
#      cd De + tab         

##################################################################
