# 문제9.  
# 사용자로부터 정수 3개를 입력받아 아래를 수행하세요. 
# 1. 세 수 중 가장 큰 값 출력 
# 2. 세 수의 평균 계산 
# 3. 평균이 70 이상이면 "통과", 아니면 "불합격" 출력 
# 4. 평균이 정수인지 실수인지 판단하여 "정수 평균" 또는 "실수 평균" 출력 
# (힌트: float은 소수점 아래가 있어요. 즉. 나눗셈의 나머지값이 있어요.  ) 

a = int( input('1st 입력 정수'))
b = int( input('2nd 입력 정수'))
c = int( input('3rd 입력 정수'))

max_value = a if( a>b and a>c) else b if(b>a and b>c) else c 

print("입력한 세 수 중 최대값은{}".format(max_value))
mean_value = (a + b + c) / 3
mean_value_mod = (a + b + c) % 3
print("입력한 세 수의 평균은{}".format(mean_value))

if mean_value>=70:
    print('통과')
else:
    print('불합격')

if mean_value_mod == 0:
    print('정수 출력')
else:
    print('실수 출력')
 
 

