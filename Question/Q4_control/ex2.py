# 문제2. 
# 사용자로부터 정수 2개를 입력받아서 둘 중 작은 값을 구하여 출력하는 프로그램을 
# 작성하시오.  
# 단, 같은 값이면 그 값이 출력되도록 하시오. 

user_input_integer1=0
user_input_integer2=0

for n in range(2):
    if not n:
        user_input_integer1 = int( input("입력값1:>>>"))
    else:
        user_input_integer2 = int( input("입력값2:>>>"))

if user_input_integer1 > user_input_integer2:
    print(f"두 키중 작은 값은: {user_input_integer2}입니다.")
elif user_input_integer1 < user_input_integer2:
    print(f"두 키중 작은 값은: {user_input_integer1}입니다.")
else:
    print(f"두 키는 같은 값: {user_input_integer1}=={user_input_integer2}입니다.")

print()

        
