# 함수를 선업합니다.
# 작성은 내가 하고 검증은 ai한테 물어봐라.
# 개발자가 layoff 되었지만 지금 다시 복귀중이라고 함.
# ai를 활용하는 사람이 우리를 대체하는 것이다. 

#함수는 항상 앞쪽에 먼저 선언이 되어야 함. 
def sum_all(start=0,end=100,step=1): # 기본변수(파라미터)
    #변수를 선언합니다.
    output = 0   # 지역변수 
    # 반복문을 돌려 숫자를 더합니다.
    for i in range(start,end+1,step): # range라는 함수에서 값을 빼낼수 있는 iteraable 이다.. 이것은 나중에 형변환 해야 함.
        output +=i 
    #리턴합니다.
    return output  # 지역변수의 값을 리턴함. 



#함수를 호출합니다. 
#함수 밖에서는 전역변수 
print("A: ",sum_all(0,100,10)) # 일반변수 호출
print("B:",sum_all(end=100)) # 일반변수를 주지 않아도 함수 원형이 default값을 가지고 있어 에러가 안남. 
print("C:",sum_all(end=100,step=2)) 
