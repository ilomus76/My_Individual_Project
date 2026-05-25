# 문제1. 

# 세 개의 정수를 인자로 전달받아서 그 중 가장 큰 수를 반환하는 함수와 가장 작은 수를 

# 반환하는 함수를 정의해 보자. 그리고 이 함수를 호출하는 프로그램도 작성해보자. 

# [파이썬 내장함수 min, max를 직접 만들어 보아요. 함수의 이름은 각자 적절한 식별자를 

# 명명하시오.] 


def cal_high_value(a=0,b=0,c=0):
    # 지역변수 선언
    highest = max(a,b,c) # 가변매개변수 인자를 사용하는 max
    lowest  = min(a,b,c) # 가변매개변수 인자를 사용하는 min
    return highest,lowest # return 값으로 두가지의 , 으로 분리된 값을 사용하는 것은 tuple임.

# 전역 영역
high_value, low_value = cal_high_value(3,19,7)
print('반환 받은 가장 큰값:',high_value)
print('반환 받은 가장 작은값:',low_value)