# 문제9. 
# 사용자로부터 5개의 단어를 ,(콤마)를 구분자로 하여 입력받아, 그 중 문자 길이가 5 
# 이상인 단어만 출력하세요. (hint. 입력된 문자열은 1개임- 1개의 문자열안에 콤마가 
# 여러개인 것임. ) 
# 예) 
# 입력: apple, cat, banana, hi, study 
# 출력: 
# apple 
# banana 
# study 

user_input = input("5개의 단어를 ,로 구분하여 입력하세요: >>> ")
user_input_word_list = user_input.split(',')
#print(user_input_word_list)

for s in user_input_word_list:
    if len(s.strip())>=5:
        print(s.strip())

