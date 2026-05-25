# 변수와 자료형 및 키보드 입력기능 : input() 과제 
# 문제 1. 자기소개 출력하기 
# print() 함수를 사용해 아래 내용을 출력해보세요.  
# 단 [이름],[음식]은 변수로 만들어 본인의 이름과 좋아하는 음식을 저장한 후 
# 출력하세요. 
# 안녕하세요! 저는 [이름]입니다. 
# 좋아하는 음식은 [음식]입니다. 
# 출력 예) 
# 안녕하세요! 저는 민수입니다. 
# 좋아하는 음식은 피자입니다. 

# 코멘트 하고자 하는 영역을 잡고 ctrl + / 을 누르면 주석처리되고 해당 부분을 다시 ctrl+/하면 주석이 풀림.

# snake case method(expression)
personal_name = input("본인의 이름을 입력하세요: ") 
# snake case method(expression)
food_name = input("당신이 좋아하는 이름을 입력하세요: ")
print("안녕하세요! 저는", personal_name,"입니다.-기본 print 방식 출력")
print("안녕하세요! 저는 {} 입니다.-formatting 방법".format(personal_name))
print(f"안녕하세요! 저는 {personal_name} 입니다-f-string 방법.")
print("좋아하는 음식은",food_name,"입니다.-기본 print 방식 출력")
print("좋아하는 음식은 {}입니다-formatting 방법".format(food_name))
print(f"좋아하는 음식은 {food_name}입니다-f-string 방법")