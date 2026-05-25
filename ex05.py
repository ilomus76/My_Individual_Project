#p112 to p 
# 변수 선언과 할당
pi = 3.14
radius = 10

# 변수 참조
print("원주율 =",pi)
print("반지름 =",radius)
print("원의 둘레 =",2*pi*radius) # 원의 둘레
print("원의 넓이 =",pi*radius*radius) # 원의 넓이 
# 실수의 계산 결과는 소수점 15자리로 double형으로 표시 : 62.800000000000004

a = 10
a +=10
print("a+=",a)

str_word = "안녕하세요"
str_word += "!"
str_word += "!"
print("string:",str_word)

# 사용자 입력
# input()
input("문자를 입력하세요>")
input()
str_input = input()
print("str_input:{} str_input_type:{}".format(str_input,type(str_input)))

str_input = input("숫자를 입력하세요>:")
print("str_input:{} str_input_type:{}".format(str_input,type(str_input)))