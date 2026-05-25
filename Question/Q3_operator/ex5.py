# 문제5. 
# 현재 시간(시,분,초)를 각각 정수형 변수에 입력받아 오늘 00시 00분 00초를 기준으로 
# 몇 초가 흘렀는지를 계산하는 프로그램을 작성하시오. 

hour = int( input("현재의 시간값을 입력하시오: > "))
min  = int( input("현재의 분값을 입력하시요  : >"))
second = int( input("현재의 초값을 입력하시요: > "))


time_difference = hour*60*60 + min*60 + second - 0

s = "현재의 시간은 {:2d}시{:2d}분{:2d}초이고 자정을 기준으로 {:10d}초가 흘렀습니다.".format(hour,min,second,time_difference)
print(s)