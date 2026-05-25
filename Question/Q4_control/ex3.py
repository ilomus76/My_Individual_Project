# 문제3. 
# 사용자로부터 정수 3개를 입력받아 정수형 변수 a, b, c 에 각각 저장한 후, 조건문을 
# 사용하여 이들 변수 중 가장 큰 값을 가진 변수의 값을 max라는 이름의 정수형 변수에 
# 대입하고 출력하는 프로그램을 작성하시오. 

a = int( input("input1:>>>"))
b = int( input("input2:>>>"))
c = int( input("input3:>>>"))

if  a>b and a>c:
    temp_max=a
    print(f"입력한 값중 가장 큰 값은 {temp_max}입니다.")
elif b>a and b>c:
    temp_max=b
    print(f"입력한 값중 가장 큰 값은 {temp_max}입니다.")
else:
    temp_max=c
    print(f"입력한 값중 가장 큰 값은 {temp_max}입니다.")



