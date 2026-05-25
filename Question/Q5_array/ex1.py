# 배열 ( List, Tuple, Dictionary ) 과제 
# 문제 1. 
# 빈 리스트(요소가 없는 리스트)를 만들고 프로그램 사용자로부터 총 5개의 정수를 입력 
# 받아 리스트에 추가해보자.  
# 그리고 입력이 끝나면 다음의 내용을 출력하도록 예제를 작성해보자. - 입력된 정수 중에서 최대값 - 입력된 정수 중에서 최소값 - 입력된 정수의 총 합 

user_list = []  # initialize the list as blank value

# add the element into the empty list by getting the user value.

for n in range(5):
    temp = int( input("정수를 입력: >>  ") )
    user_list.append(temp)
    print(user_list) # using list reference data 

print(min(user_list))
print(max(user_list))
print(sum(user_list))
