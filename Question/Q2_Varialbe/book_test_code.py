#입력을 받습니다.
#string = input('입력 :')

# #출력합니다.
# print("자료:",string)
# print("자료형:",type(string))


# #입력을 받습니다.
# string = input("입력> ")
# #출력합니다.
# print("입력 + 100:",string +100) # error , string + number 는 수행이 되지 않음. 



# string_a= input("입력A>") 
# int_a = int(string_a)

# string_b =input("입력B>")
# int_b=int(string_b)
# ㅇ
# print("문자열 자료: ", string_a + string_b)
# print("숫자 자료:", int_a + int_b)


# input_a = float(input("첫번째 숫자>"))
# input_b = float(input("두번째 숫자>"))

# print("덧셈 결과:", input_a + input_b)
# print("뺄샘 결과:", input_a - input_b)
# print("곱셈 결과:", input_a*input_b)
# print("나눗셈 결과:",input_a/input_b)

# output_a = str(52)
# output_b = str(52.273)
# print(type(output_a),output_a)
# print(type(output_b),output_b)


# 숫자를 입력받습니다.
raw_input = input( "inch 단위의 숫자를 입력해주세요: ")

# 입력받은 데이터를 숫자 자료형으로 변경하고, cm 단위로 변경합니다.
inch = int(raw_input)
cm = inch * 2.54

# 출력합니다.
print(inch,"inch는 cm 단위로",cm,"cm입니다.")