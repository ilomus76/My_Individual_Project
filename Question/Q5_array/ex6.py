# 문제 6. 
# 2차원 좌표값은 튜플(x, y) 형태의 데이터를 사용합니다. 
# point1 = (2, 3) 
# point2 = (5, 7) 
# 1. point1의 x좌표만 출력하시오. 
# 2. point2의 y좌표만 출력하시오. 
# 3. 두 좌표 간의 거리(유클리드Euclidean 거리)를 계산하시오.[ML 유사도 계산에 
# 사용되는 거리값] 
# 유클리디안 Euclidean 거리 공식: 

point1=(2,3)
point2=(5,7)
print("x position of point1 : ", point1[0])
print("y position of point2 : ", point2[1])

temp=0
for e in range(2):
    temp +=(point1[e]-point2[e])**2

print("두 좌표 간의 거리(유클리드Euclidean 거리)", temp**(1/2)) 