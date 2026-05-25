# 함수를 선업합니다.
# 작성은 내가 하고 검증은 ai한테 물어봐라.
# 개발자가 layoff 되었지만 지금 다시 복귀중이라고 함.
# ai를 활용하는 사람이 우리를 대체하는 것이다. 

#함수는 항상 앞쪽에 먼저 선언이 되어야 함. 
def sum_all(start,end):
    #변수를 선언합니다.
    output = 0   # 지역변수 
    # 반복문을 돌려 숫자를 더합니다.
    for i in range(start,end+1): # range라는 함수에서 값을 빼낼수 있는 iteraable 이다.. 이것은 나중에 형변환 해야 함.
        output +=i 
    #리턴합니다.
    return output  # 지역변수의 값을 리턴함. 



#함수를 호출합니다. 
#함수 밖에서는 전역변수 
print("0 to 100: ",sum_all(0,100))
print("0 to 1000:",sum_all(0,1000))
print("50 to 100:",sum_all(0,100))
print("500 to 1000:",sum_all(500,1000))