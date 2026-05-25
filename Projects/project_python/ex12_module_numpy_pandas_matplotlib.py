# 데이타를 수집했다면.. 분석해야 함.
# 데이터분석을 ㄹ쉽게 해주는 대표적인 외부 모듈 : numpy, pandas
# 보기편하게 시각화 (그래프) 해주는 외부 모듈: matplotlib


# 0) 외부 모듈 설치
# pip install numpy
# pip install pandas
# pip install matplotlib
# 띄어 쓰기 하면 하나씩 다 다운로드 된다고 함.


#1) numpy (numberic python) : 배열같은 대량의 데이터를 행렬 수학계산 해주는 기능모듈  : 벡터곱. 행렬
# (10,20) + (30,40)

# 모두 설치했으면 pin list로 모듈이 설치 되었는지 확인..
# 나머지는 깔면서 연동된것이 같이 깔림.


# exit으로 터미널 나옴. 

# 파이썬에서는 수학이 안됨. 

# 1. 일반적인 파이썬의 배열(리스트 , 파이썬에서는 배열이라고 사용안함.)
aaa = [10,20,30]
bbb = [4,5,6]

# 파이썬의 배열(리스트)는 덧셈을 하면 산수덧셈이 아니라. concat(): concatenate 이 되어 요소가 추가됨
ccc = aaa + bbb 
print(ccc) 
# 이것은 산수 더하기가 아니라 결합이 됨.

#2. numpy 배열로 만들어서.. 산술 덧셈을 수행
import numpy as np 
#aa= numpy.array([10,20,30]) # 넘파이야 너가 배열을 만들어줘 . 이것은 파이썬의 리스트를 넘파이의 배열로 만듬. 
# 리스트를 numpy용 배열자료형으로 만들기
aa= np.array([10,20,30]) # 넘파이야 너가 배열을 만들어줘 . 이것은 파이썬의 리스트를 넘파이의 배열로 만듬. 
bb = np.array([4,5,6])
#배열끼리 산술 덧셈
cc = aa + bb # [14 25 36]
print(cc)

# 사칙연산 모두 가능
print(aa-bb) #[ 6 15 24]
print(aa*bb) #[ 40 100 180]
print(aa/bb) #[2.5 4.  5. ]
# 사칙연산 말고도 많은 수학적 기능을 가지고 있지만...2부 수업에서 정식 소개
print()
#--------------------------------------------------------

#2) pandas : 엑셀이나 , CSV 처럼 표형태의 데이터를 실제 표처럼 쉽게 다룰 수 있도록 해주는 모듈 ( 매우 많이 사용. 우리의 주력)
import pandas as pd

# csv 파일을 읽어와서 행열 표형태(DataFrame이라고 부름)로 만들어 줌.
aa = pd.read_csv('Projects/files/scores.csv')
print(aa)
print()
#5교시 

# 우리 csv에는 0,1,2라는 인덱스가 없는데 판다스를 사용하면 이것이 만들어짐.

print(aa.head()) # 상위 5개만 추출 
print(aa.tail()) # 하위 5개만 추출
print(aa.head(n=2)) # 상위 2개만 추출
print(aa.shape) # 행렬 모양(개수 확인)
# 국어 성적만.. 확인.

print(aa['국어'])  # 인덱스와  dtype: int64 처럼 데이타 타입도 출력됨.

# 칸 제목들 확인
print(aa.columns)

# 데이타분석에 필요한 기초 계산을 해줌(집계 함수)
print('korean average:', aa['국어'].mean()) # 국어 평균 
print('english maximum:',aa['영어'].max()) # 영어 최고값

#기초 계산들을 모듀 해주는 기능(평균, 최대값 , 중위값... 25% 해당 값 등.. 을 모두 알려줌.)
print(aa.describe())

#std : 표준편차 standard deviation 

# 특정 학생의 성적들 추출(특정 행 (row:줄))
row =aa.loc[0] # 맨위의 첫번째
print(row)

rows = aa.loc[1:3] # 1~3까지...
print(rows)
print()

rows = aa.loc[2:,['이름','수학']] # 2번부터 끝까지, 이름하고 수학만..
print(rows)
print()
# ----------------------------------------------------


# 꽤 많은 회사에서 데이터들을 엑셀파일로 가지고 있는 경우가 많음. 
# 엑셀은 vS code에서 열지 못함. 

# 원래 엑셀은 꽤 읽기 어려움...
# 다행히 엑셀파일을 파이썬에서 쉽게 읽어오는 외부모듈 존재함. [openpyxl]
# [설치] : pip install openpyxl
# 확인 pip list , 종료 : exit

# pandas 가 엑셀 파일을 읽어들일때.. openpyxl 모듈을 사용함. 
bb= pd.read_excel('Projects/files/student_scores.xlsx')
print(bb)
print()
#분석하는 방법은 위 csv 때와 똑같이 수행가능.

print(bb.describe())
print()

#---------------------------------------------------

#3) matplotlib : matlab plot library에서 나옴. : 파이썬에서 데이터를 눈으로 보기 쉽게 시각화하는 모듈
# 숫자가 있는 모든 데이터를 표현 가능 [ 선 그래프, 막대그래프, 원그래프 등.. 많은 종류 보유]

#1. 모듈 사용
import matplotlib.pyplot as plt  # 원래 c 언어로 만들어짐... 이제는 파이썬으로 됨. 하위 폴더에 있음. 

# 그래프에 한글이 깨지지 않도록... 한글 글꼴을 지정. 
plt.rcParams['font.family']='Malgun Gothic' # 컴퓨터에 내장된 글꼴을 의미
# rc : runtime configuration 

#[1] 하루동안의 온도변화 그래프----------------------------------------
#2. 데이타 준비 
# 시간별 온도 

hours = [6,9,12,15,18,21,24]                   # 그래프의 x축 데이터

temperature = [10,14,18,20,17, 13,11]          # 그래프의 y축 데이터

#2부 수업에 하는 것이 이런것이다. 
#3. 그래프 그리기 
#plt.plot(hours, temperature)
# plt.plot(hours, temperature, marker ='o')
# plt.plot(hours, temperature, marker ='x')
# plt.plot(hours, temperature, marker ='v')
plt.plot(hours, temperature, marker ='v',linestyle='--',color='orange')

# 그래프 꾸미기
plt.title('하루 동안의 온도 변화') # 한글은 깨진다.. 문제는 글꼴이 문제임. 
plt.xlabel('시간')
plt.ylabel('온도')
plt.grid(True)

#4.그래프 표시 
plt.show()

#--------------------------------

#예제2)

# 1. 롯데리아 월별 매출 데이터 준비 (가상)
data = {
    '월': ['1월', '2월', '3월', '4월', '5월', '6월', '7월', '8월', '9월', '10월', '11월', '12월'],
    '매출액(만원)': [4200, 3900, 4500, 4700, 5200, 5800, 6100, 6400, 5900, 5500, 5300, 5000]
}

# 위 dict를 판다스로 아주 쉽게 표로 만들 수 있음. 
ee = pd.DataFrame(data)
print(ee)

# 그래프로 시각화 하기
plt.figure(figsize=(8,5)) # 도화지 사이즈 : 가로가 긴 그래프 ,설정안하면 가로 세로 같게 나옴. 

#산점도 그래프 표시 : 산재된 그래프.. scatter graph

plt.scatter(ee['월'], ee['매출액(만원)'],marker = 'o', color = 'tomato') # x축 , y축 plot   bar : 막대, histogram : 히스토그램

# 그래프 꾸미기
plt.title('롯데리아 2026년 월별 매출 변화')
plt.xlabel('월')
plt.ylabel('매출액 (만원)')
plt.grid(True)

# 각 점마다 매출액 값 표시하기
for idx,value in enumerate(ee['매출액(만원)']):
    #plt.text(idx,value,'aa') # aa값을 idx,value에 찍는다. 
    #plt.text(idx,value+50,'aa') # aa값을 idx,value에 찍는다. 
    #plt.text(idx,value+50,'aa', ha='center',fontsize=9) # aa값을 idx,value에 찍는다. 
    plt.text(idx,value+50,f"{value}", ha='center',fontsize=9) # aa값을 idx,value에 찍는다. 
                           


#그래프 출력
plt.show()





