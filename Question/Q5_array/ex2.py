# 문제 2. 
# 사용자로부터 정수형 숫자 하나를 입력받자. 이 입력된 숫자 만큼 사용자로 부터 
# 문자열을 입력받아 리스트에 저장하도록 해보자. 
# 입력된 문자열들이 잘 저장되어 있는지 확인하기 위해 배열의 각 요소들을 for in 
# 반복문으로 차례로 출력해보자. 

user_input = int ( input('정수 하나를 입력하시오.>>>  ') ) # int (형변환) -> 형변환 되는 것은 문자열 
# the variable is initialized by getting any data .

string_value = "" # blank string 

temp = input('당신이 입력한 숫자만큼 글자를 넣으시오. >>>> ')
for c in range(user_input):
    string_value += temp[c]

print(string_value)
    