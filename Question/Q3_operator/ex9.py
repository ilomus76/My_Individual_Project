# 문제2. 
# 'I love Python programming'이라는 문자열에서 'Python'만 추출하여 출력하세요.  
# 문자열 데이터 변수 : sentence = "I love Python programming" 


s = " I love Python programming"
a = s.find("Python")
print(a)
print(s[a:a+len("Python")])

