# 문제2. 
# 아래와 같은 문자열을 가진 변수가 있다. 문자열을 소문자로 바꾸고, 양쪽 공백을 
# 제거하는 코드를 작성하세요.  
# whitespace_string = "  PYTHON   "


s = ' whitespace_string = "  PYTHON   '
print(s)
b = s.lower().strip()
print(b)