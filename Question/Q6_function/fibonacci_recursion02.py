#변수를 선언합니다. 
counter = 0

#함수를 선언합니다.
def fibonacci(n):
    #어떤 피보나치 수를 구하는지 출력합니다. 
    print('fibonacci({})를 구합니다'.format(n))
    global counter # 전역변수가 있는데 그것의 값을 지역변수에서 바꾸면 전역변수는 지역변수로 바뀜. 이를 방지하여 전역변수를 사용하려면 global이라는 선언을 먼저 해줘야 한다.
    
    counter +=1
    #피보나치 수를 구합니다.
    if n==1:
        return 1 
    if n==2:
        return 1
    # n이 0이 아니라면 n*(n-1)을 리턴 
    else:
        return fibonacci(n-1)*fibonacci(n-2)
     

#함수를 호출합니다.

fibonacci(10)
print("---")
print("fibonacci(10) 계산할 때 함수를 호출한 횟수는 {}번입니다.".format(counter))
