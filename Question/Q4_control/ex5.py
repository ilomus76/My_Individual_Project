# 문제5. 
# 문제 4번의 내용을 if~else를 사용하여 해결하였는가? 이를 if~else의 한줄쓰기 
# 문법인 삼항연산자를 이용하여 구현해 보자.    (A if(조건) else B)


a = int(input("입력1:>>>>"))
b = int(input("입력2:>>>>"))

c= a-b if(a>b) else b-a

print(f"입력한 두수 {a}와 {b}의 차이는: {c}입니다.")

# if c>0:
#     print(f"입력한 두수 {a}와 {b}의 차이는: {c}입니다.")
# elif c<0:
#     print(f"입력한 두수 {a}와 {b}의 차이는: {-c}입니다.") 
# else:
#     print(f"입력한 두수 {a}와 {b}의 차이는: {c}입니다.")    
