# format()함수로 숫자를 문자열로 변환하기
# snake case 
string_a = "{}".format(10) # 숫자 10을 {}안에 넣어 포맷을 만들어 변수로 대입.

#출력하기
print(string_a)
print(type(string_a))


format_a = "{} 만 원 ".format(5000)
format_b = "파이썬 열공하여 첫 연봉 {}만 원 만들기".format(5000)
format_c = "{} {} {}".format(3000,4000,5000)  # tuple 로 인식...
format_d = "{} {} {}".format(1,"문자열",True)

#출력하기 
print(format_a)
print(format_b)
print(format_c)
print(format_d)

#indexError 

# 정수
output_a = "{:d}".format(52)

#특정 칸에 출력하기 
output_b = "{:5d}".format(52)  # 5칸
output_c = "{:10d}".format(52) # 10칸


# 빈칸을 0으로 채우기
output_d = "{:05d}".format(52)  # 양수 
output_e = "{:05d}".format(-52) # 음수 

print('# 기본')
print(output_a)
print('#특정칸에 출력하기')
print(output_b)
print(output_c)
print("# 빈칸을 0으로 채우기")
print(output_d)
print(output_e)


#개호와 함께 출력하기.
output_f= "{:+d}".format(52) # 양수 
output_g= "{:+d}".format(-52) #음수 
output_h= "{: d}".format(52) #양수 : 기호 부분 공백
output_i= "{: d}".format(-52) #음수 : 기호 부분 공백
print(output_f)
print(output_g)
print(output_h)
print(output_i)

#조합하기
output_h= "{:+5d}".format(52) # 기호를 뒤로 밀기 : 양수 
output_i= "{:+5d}".format(-52) # 기호를 뒤로 밀기 : 음수
output_j= "{:=+5d}".format(52) #기호를 앞으로 밀기 : 양수
output_k= "{:=+5d}".format(-52) #기호를 앞으로 밀기 : 음수
output_l= "{:+05d}".format(52) #0으로 채우기 : 양수
output_m= "{:+05d}".format(-52) #0으로 채우기 : 음수 

print("# 조합하기")
print(output_h)
print(output_i)
print(output_j)
print(output_k)
print(output_l)
print(output_m)

#부동소수점
output_a= "{:f}".format(52.273) # 
output_b= "{:15f}".format(52.273) 
output_c= "{:+15f}".format(52.273) 
output_d= "{:+015f}".format(52.273) 

print(output_a)
print(output_b)
print(output_c)
print(output_d)


output_a= "{:15.3f}".format(52.273) # 
output_b= "{:15.2f}".format(52.273) 
output_c= "{:15.1f}".format(52.273) 


print(output_a)
print(output_b)
print(output_c)


output_c= "{:.15g}".format(52.111) 
print(output_c)


a = "Hello Python Progrmaming...!"
a.upper() 
print(a) 




a = """ 
    안녕하세요
    저는 홍길동입니다. """

print(a)
print(a.strip())
print(a)


print("TrainA10".isalnum()) 
print("10".isdigit())

a= "오늘 중으로 image data를 만들어서 해당 data를 9시까지 제출하고 data를 책상위에 올려두세요. 참고로 상자에 DATA 라고 적혀 있어요."
b =a.find("data")
print(b)

b =a.rfind("data")
print(b)


print( "안녕" in "안녕하세요")


csv = "10 20 30 40 50 "
a=csv.split(" ")
print(a)



# 책 도전 문제 풀이
#구의 부피와 겉 넓ㅇ.

radius = input("구의 반지름을 입력해 주세요: ")
pi = 3.14
print("= 구의 부피는 {}입니다.".format(4.0*pi*(float(radius)**3)/3))
print("= 구의 겉 넓이는 {}입니다".format(4.0*pi*(float(radius)**2)))
      


a = input("밑변의 길이를 입력해주세요: ")
b = input("높이의 길이를 입력해주세요: ")

c = ( int(a)**2 + int(b)**2 )**(1/2)

s = " = 빗면의 길이는 {}입니다.".format(c)
print(s)