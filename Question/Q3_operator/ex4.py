# 문제4. 
# 사용자로부터 정수 3개를 입력받아서 정수 3개의 합, 평균을 구해서 출력하는 프로그램을 
# 작성하여 보자. 단, 평균은 소수점이하의 숫자도 출력되도록 한다.    

key_a = int(input("입력값 : A >"))
key_b = int(input("입력값 : B >"))
key_c = int(input("입력값 : C >"))

sum = (key_a + key_b + key_c)
mean = sum/3 

s="입력한 세 값 {:d},{:d},{:d}의 합은 {:d}이고 평균은{:=+.5}입니다".format(key_a,key_b,key_c,sum,mean)
print(s)