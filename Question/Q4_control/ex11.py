# 문제11. 
# 다음과 같은 형식의 문장을 visited 변수에 저장되어 있다. 
# visited = '오늘 방문자 수는 350명이었고, 어제는 280명이었다.' 
# 1. 문장 안에서 숫자로 이루어진 부분(예: "350" , "280")을 직접 찾아 정수로 
# 변환하여 두 수의 차이를 출력 하시오. 
# 2. 오늘이 더 많으면 "증가", 적으면 "감소" 
# ※ 리스트 사용 없이 문자열 처리만으로 해결해야 함. 
# (hint: ‘명’자를 찾아서 그 앞의 숫자를 찾아냅니다. ‘ ‘공백문자를 찾아서 숫자의 길이 
# 계산)  

visited = '오늘 방문자 수는 350명이었고, 어제는 280명이었다.' 
texta=visited.strip()
text_a = texta.find("명")
print(text_a)

text_b = texta.find("명",text_a)
print(text_b)

#c= int(visited[text_a-4:text_a-1]) - int(visited[text_b:text_b-1]) 

print(int(visited[text_a-4:text_a]))
print(int(visited[text_a+text_b-4:text_a+text_b]))


c= int(visited[text_a-4:text_a])-int(visited[text_a+text_b-4:text_a+text_b])

if c>0:
    print("증가")
    print("diff:",c)
else:
    print("감소")
    print("diff:",-c)

# visited_rearrage=visited.strip()
# today = visited_rearrage.find("명")
# print(today)
# yesterday = visited_rearrage.find("명",today+1)
# c= int(visited[today-1])-int(visited[yesterday-1])

# print(c)

# if today>yesterday:
#     print(f"두수의 차이 : {today}, {yesterday} {today-yesterday}")
#     print(f"두수의 차이 : {visited[today-1]}, {visited[yesterday-1]} {c}")
#     print("증가")
# else:
#     print(f"두수의 차이 : {today}, {yesterday} {today-yesterday}")
#     print(f"두수의 차이 : {visited[today-1]}, {visited[yesterday-1]} {-(c)}")
#     print("감소")  



