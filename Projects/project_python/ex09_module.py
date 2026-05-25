# 모듈 : 코드를 쓸때 하나의 py 파일에 모든 코드를 작성하면 기능별로 관리하거나 재사용하기 어려움.
# 모듈은 여러개의 변수와 함수를 가지고 있는 코드 파일의 집합체

# 모듈의 종류 
# 1) 표준모듈 - 표준함수와 다름.  : 파이썬에 기본으로 내장되어 있어서 별도의 다운로드 설치 필요없이 import만 하면 사용가능 [ 표준함수는 아님. 즉 import 해야함.]
# 디렉토리 안에 숨겨 놓았다고 보면 된다. 
# 2) 외부모듈 : 파이썬 설치 할때 같이 설치된 pip 으로 다운로드 설치 후 import하여 사용 
# pip - > CLI 로 구성된 패키지 인스톨러 프로그램 : 소프트웨어 == 프로그램 == 패키지... 같은말... 
# openpyxl 이라는 모듈을 다운받고 싶어... 
# > pip install openpyxl 이라고 치면 openpyxl기능이 생김.
# > pip instal tensorflow 
# PIP (package installer for python) : 파이쎤 전용 인스톨러... 파이썬 라이브러리들만...
# 자바스크립트도 npn이라는 인스톨러가 따로 있다.
# 맥 혼브로, 윈도우 초코렛티....  이런것들이 cmd 에서 명령어를 쳐서 다운로드 함.... CLI installer programd이라고 함. 



# 오늘은 표준모듈만 할 것임

# 먼저 표준모듈 중 활용이 많은 모듈들... 
#1. math 모듈 : 수학헉 연산기능(함수)을 모아놓은 모듈 : ~ ML 머신러닝에서 많이 활요
# 모듈을 다루는 것이 어떤지 감으로 느껴라..

import math # 모듈 적용 하는 모습 

print( math.sin(1))
print( math.cos(1))
print( math.log(100,10)) # 로그값( (log 10 1000)) 10에 몇승을 하면 100이게 ? ( x, 밑수) 10의 몇승을 하면 100일까? 
print( math.log(8,2)) #로그값 (x, 밑수) 2의 몇승을 하면 8일까?
print( math.floor(3.7)) # 소수점 내리기 [ floor : 바닥] - 반올림 이 아님. -> 3 
print( math.ceil(3.2)) # 소수점 올리기 [ ceil : 천장 ] - 무조건 올림 -> 4 
# 반올림은 math 모듈을 사용하지 않고... 표준함수 round() 를 이용. 즉 import 없이 사용.

print( round(3.7)) # 사사오입 : 4는 내리고 5는 올리고..
print( round(3.2))


# 함수가 아닌 값을 가진 변수도 모듈안에 존재함.
print(math.pi) #변수
# --------------------------------------------------

#1.1 모듈의 기능을 사용할 때 마다 math 라는 모듈명을 쓰고.. 함수명을 쓰기에 .. 좀 번거로워....
# 모듈명이 길면.. 더 짜증날듯...
# 그래서 import 하면서 module 명을 다르게 바꿔 부를 수 있음. 

import math as m 
print( m.pow(4,3)) # 4의 3제곱  : 4**2

#1.2 모듈안에 있는 중에서 매우 자주 사용하는 기능이 있다면.. 모듈명을 쓰는것 조차 번거로움. 
# import 할때 ... 표준함수처럼.. 함수명만 쓰면 되도록... 모듈 전체가 아닌 함수만 import할수 있음.

from math import floor,ceil, pi  
print( floor(3.7)) 
print()
#------------------------------------------------------------

#2. random 모듈 : 랜덤값 제공 기능을 가진 모듈 
import random 
print(random.random()) # 0.0 ~ 9.99999999 왜 값을 이렇게 내뱉을까? 숫자의 범위가 너무 넓어 한정함.... 0부터 10사이는?
print(math.floor(random.random()*10)) # 0부터 10사이는? 코드 쓰기 힘듦.
print(random.randrange(10)) # 0~9 까지 정수 중 랜덤
print(random.randrange(5,16)) # 5~15 까지 정수 중 랜덤

# 리스트 요소중 랜덤하게 값을 선택...
aaa = [10,20,30,40,50]
print(random.choice(aaa)) # 1개 선택,,, random아 aaa값중 하나를 선택해줘... 
print(random.sample(aaa,3)) # 3개 선택 -- 리스트로 결과를 줌. 

# [예] 로또 번호 추전...
lotto = list ( range(1,46)) # 1,2,3,4....,45
print(lotto)

# 로또 번호 45개중 6개를 랜덤하게 선택 
nums = random.sample(lotto,6) # 랜덤아.. 내가 로또 번호를 줄게 6개중 뽑아줘..
print(nums)

# 낮은 번호 순으로.. 정렬
nums.sort()
print(nums)
print('='*20)
print()
#-------------------------------------------------------

#3. os 모듈 : operating system : 운영체제와 관련된 기능 모듈 
import os  # 디렉토리 만들고 하는 것듯.

print('현재 작업폴더:',os.getcwd()) # get current working directory  
print('현재 폴더목록:',os.listdir()) # 현재 폴더의 파일 및 폴더 목록 

# 폴더 만들기 
# 파일 오픈시 폴더는 만들어 주지 않았음.
#os.mkdir('image') # 이미 있는 경우 에러가 남. 
#존재하는 폴더명을 다시 만들려고 하면 에러!! 그래서 존재하지 않을때만 만들도록...
if not os.path.isdir('image'): # 너의 경로 명에 image라는 게 있냐? 
    os.mkdir('image')

#4교시
#폴더 삭제하기
if os.path.isdir('image'): # os에 path가 있는지,, 디렉토리 이미름 image 인지...
    os.rmdir('image')

# 파일명 변경해 보기
if os.path.exists('aaa.txt'): #os의 경로중에 존제하니...aaa.txt가? 
    os.rename('aaa.txt','new name.txt')

# 폴더 위치 이동.
print("현재 폴더 위치",os.getcwd())
os.chdir('..') # 상위 폴더로.... 
print("현재 폴더위치:",os.getcwd()) 
os.chdir('Python')
print("현재 폴더위치:",os.getcwd()) 

# cmd 나 터미널 창에서 작성했던 대부분의 명령어들 파이썬 코드로 실행시킬 수 있음. 
os.system('dir') # 터미널에 dir 명령어를 쓰는 것과 같은 기능. 
os.chdir('Projects')
os.system('python ex01_print.py') # 다른 파이썬 파일 실행도 가능.
os.chdir('..') 

# 함수를 사용하는 취소선같은 것이 보인다면.. 더이상 사용을 권장하지 않는 다는 뜻. - deprecated(회피하다) 되었다고 함.
# 파이선 1버전부터 있었음. 버전이 올라오면서 취약함이 나옴. 보안상 이슈, 리소스 낭비가 보임...
# 동작은 되고 아직은 써도 되지만 지금은 개도 기간이고 조금 지나면 저것은 아예 쓰지 못한다..임.
# subprocess로 대체되었다... 
import subprocess   # 최근에 생김.
subprocess.run('dir',shell=True) # 컴퓨터와 대화하는 것,, 파이썬 인터렉티브 쉘이 필요하면 써라..
os.chdir('Projects')
subprocess.run('python ex01_print.py',shell=True)  
print('-'*30)
print()
#------------------------------------------------------------

# 날짜 시간 ...
#4. datetime 모델 : 날짜와 시간 관련 기능 제공하는 모듈 
import datetime 

#현재 날짜와 시간 얻어오기 : 명령 내리는 시간 
# 객체가 있음 : 변수와 함수를 포험. 
now = datetime.datetime.now()
print(now) 
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second) # 실행할대 그 순간에 시간.
print()

# 특정 시간 변경 기능
future = now.replace(year=(now.year+1)) # 문자열 글자 바꾸기에서 봄 
print(future)
print(now) # 원본 안바뀜
print()

# 경과시간 같은 것을 계산해야 하는 경우가 있음.....
# 경과 시간을 계산하기 편하게... 시간의 기록을 카운팅한 값이 존재함. 
print(now.timestamp()) # 카운팅... 1970-01-01 0:0:0 초부터 밀리세컨드 마다 카운팅된 값 
# 1778731181.462114 초
print()

# 타임스탬프로 기록값 숫자를 통해 특정 작업이 얼마나 시간이 소요되었는지 확인 가능


start = datetime.datetime.now() # 이 순간의 시간....
#특정작업 !!!
for n in range(10000):
    print(n,end=' ')
print()

end = datetime.datetime.now() # 이순간의 시간


# 경과시간 계산.. 종료시간 - 시작시간
elipsed_time = end - start 
print('경과시간:', elipsed_time) 


# 날짜 계산 프로그램 만들기.
a_day = datetime.datetime(2026,4,29) #특정 날짜 만들기
today = datetime.datetime.now()
print('개강일로 부터: ' , today - a_day)
print('개강일로 부터: ' , (today - a_day).days,'일 경과')
print("-"*30)
print()

#5.time 모듈 
import time
print('3초간 프로그램을 정지하기.... 잠시만 기다려 주세요...')
time.sleep(3)
print('프로그램이 다시 시작됩니다.')

# 타임스탬프로.... 더 간단하게.... 
print(time.time()) # 1778731921.4186704 


print(time.time_ns()) # nano second 단위 
#---------------------------------------------------------------

#6. urllib 모듈: url (인터넷주소) , lib :라이브러리 
# URL ( Uniform Resource Location) - www.naver.com , 특정 위치 , 정보에 대한 내용 
# URL 관련 기능 제공 모듈 

# 인터넷 작업은 처리 데이타가 방대해서...
# 서버에서 요청하는 것만 모아 둠. 
# 그래서 하위모듈 ( 디렉터리 안에 디렉토리) 도 import해야 함...  
# urlopen() -> 인터넷 파일을 열어라... naver    -> 네이버 코드를 써서 만듬. 즉 문서임. .html 임 .. 단 그게 인터넷에 있음. 

from urllib import request 
url = request.urlopen('https://www.naver.com')
# 실제로 서버에 요청해서 서버에서 오는 데이타 패킷을 받는것임. 컴퓨터에 다운 받은 웹페이지를 가져오는 것이 아니라...
data = url.read()
print(data) 
# 마치 file open 하는 것과 비슷함. 

#가져와서 뭐할 것이냐?

