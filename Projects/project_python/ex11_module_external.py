# 1교시
#외부 모듈 - 개발자나 업체에서 특정 기능들을 미리 작성하여 제공한 라이브러리
# 파이썬 개발환경을 구축할때 자동으로 설치되지 않기에...
# 사용하려면 사전에 다운로드 및 설치작업이 필요함.

# 이런 외부모듈은 PyPI (파이 피 아이)라는 파이썬 중앙 저장소 서버에 등록되어 제공됨. 
#우리가 만든것도 여기에 업로드 할수 있다.
# 이 서버에서 모듈을 본인 PC로 다운로드 및 설치를 쉽게 해주는 CLI 프로그램이 있음. 
# 이 모듈 설치 프로그램이 PIP(Package installer for python)임    - 모듈을 묶었다 해서 package 
# pip 는 파이썬 개발환경 구축할때 이미 함께 설치되어 있음. (에전에는 아니었다고 함)

# pip 를 이용하여 외부모듈을 설치하고 사요하는 맛보기 실습해보기 (정식수업은 python 2부 - 웹에 대한 개념이 있어야 이해가 가능)
# 파이썬 다음은 웹공부

# 외부 모듈 중 많이 사용하는 모듈 : requests , BeatifulSoup,(네트웍) Numpy , pandas ,(데이타분석) matplotlib - 매트랩에서 나온것 , 그래프, 수학적 그래프 라이브러리 (시각화), selenium(웹브라우저 자동화)

# 1. requests -- 서버데이터를 읽고 쓰는 기능 모듈 [urllib보다 고수준 모듈 --- 예외처리가 되어 다운되지 않음. 한글이 깨지는 디코딩을 자동으로 해줌. 쿠키, 세션 , 파일업로드 , JSON 형식 처리등을 자동으로 편하게 수행해줌]
# 내부적으로 try except 이 되어 있음.

#) 먼저. requests 모듈 다운로드 및 설치
# -- pip는 CLI 프로그램이어서 .. 터미널 or cmd 창에서 명령어로 설치하는 프로그램. 
# -- 터미널을 실행하고 아래 명령어를 쓰면 다운로드 및 설치가 알아서 됨 
# -- 명령어 : pip install 모듈명 - 인터넷 경로 필요없음.    terminal -> new terminal  , pip list : 뭐가 설치 되어있는지.... 확인... ( 이것으로 보면 현재 pip 만 다운 설치 되어 있는것이 확인)
#    pip install requests  ( Http protocol 규칙 쓰는데.. 내부 프로토콜 request / response 두개의 ㅍ프로토콜이 있다. 서버에 뭘 달라고 하는게 request , 서버에서 대답하는게 response)

# 이 이후 pip list로 하면 여러게 설치가 된것이 보임. 하나 설치했는데 여러개 설치되어있음.. 이유는 requests 가 혼자만 사용되는 것이 아니라 필요한 모듈을 같이 설치하기 때문.

# exit 하면 터미널 닫힘 . 혹은 휴지통 눌러라..

# pip install requests 완료 

#2) 모듈 사용 
import requests

#3) 설치가 되었으니,, 아주 쉽게 서버에 있는 텍스트문서 읽어오기 
#requests.get('서버주소 즉 서버 url') # rest 방식 ... get 방식 등등이 있다고 함..
#https://raw.githubusercontent.com/kitesoft2058/python-request-test/refs/heads/main/aaa.txt



# https 사이트의 경우 ssl 인증 모듈 추가 필요! ----------------------------
# import ssl 
# ssl._create_default_https_context = ssl._create_unverified_context
# -----------------------------------------------------------------

response = requests.get('https://raw.githubusercontent.com/kitesoft2058/python-request-test/refs/heads/main/aaa.txt') # 열고 가져와 까지 수행

# response는 글씨 데이터가 아니라 .. 응답된 데이터와 상태값을 가진 객체(여러데이타를 가진 변수 함수를 가닌 녀석)

# response 안에 정보가 많다
print(response.status_code) # 200    # 404 HTTP 에서 약속된 응답할 때 쓰는 코드 , 만약 경로가 잘못됬다고 알려주는데 그것을 숫자로 알려줌 .이것을 status code라고 함.
# 서버의 응답결과에 대한 상태값 
# 구글 Http 응답코드 검색 ...[ 200 ok, 404 Not found 경로 찾지 못함, 403 권한 없음]
# if response.status_code == 404 :

# 이 명령어를 하니 404 에러를 공지했는데 빨간색이 나타나지 않음. -> 에러처리가 되어 그러함.

print(response.text) # 응답된 글씨데이터... 한글 인코딩이 자동으로 됨. 
print() 
# 여기까지가 기본 틀.

#4) 대량의 데이터를 구분하기 용이하도록 데이타를 작성하는 파일형식 3가지(CSV,XML,JSON)중 요즘 가장 선호하는 JSON파일형식을 쉽게 분석해줌.
#  csv, xml (extensible markup language , 태그 사용 앞뒤. 스타트 태그 엔드테그 , HTML hyper text marking language 로 xml을 기반으로 만듬. 백앤드 개발자(서버개발자) - API 명세서 즉 설명서->데이타 분석에 중요)

#[2교시]
# 마치 Json은 파이썬의 dictionary 처럼 생김. 요즘은 json을 많이 사용. 자바스크립트의 객체 표기법을 바탕으로 만든 데이타 형식 

# 국가 데이타 포털에 모아두었다 .
# data.go.kr 

response2 = requests.get('https://raw.githubusercontent.com/kitesoft2058/python-request-test/refs/heads/main/hhh.json')
print(response2.status_code)  #
print(response2.text)

# 명령어를 줬는데 실행은 위에서 부터 하지만 위의 것이 실행되는 동안 덮어 쓰는 경우가 있으니 번호를 나눠 써라.

#원하는 데이터를 추출해야 함. 이를 parse라고 부름
# 응답된 json 데이터를 pytnon의 dictionary로 변환해 주면... 식별자 key 로 값을 쉽게 취득 가능

print( type(response2.text)) # <class 'str'>

data_dict = response2.json() # 리스펀스야 제이슨을 분석해서 줘 , 'str' --> 'dict'
print( type(data_dict))  # <class 'dict'> 

# dictionary 타입이기에 식별자로 원하는 값을 가져올 수 있음. 
print(data_dict['data_title'])
print(data_dict['total_count'])
print("-"*30)
print()

# -------------------------------- 1부에서는 여기까지... --------------------------------------------


# 3) 인터넷에 공개된 이미지의 URL만 주면 다운로드 해주는(내 컴퓨터에 이미지파일로 저장된다는 것) 프로그램 
address = 'https://cdn.pixabay.com/photo/2019/07/18/01/05/lotus-4345296_1280.jpg'
# pixabay : 저작권 해당 안됨. 
response3 = requests.get(address)
print(response3.status_code)
#print(response3.text) # 픽셀 데이타(2진수값)을 글씨로 읽으려 하니.. 깨짐.
#print(response3.content) # 2진수 (바이너리) 데이터를 읽어옴... 2진수는 값이 너무 길게 표시되기에 터미널에는 16진수로 변환되어 옮
# \x : hexa 데이타 

print()

# 위 바이너리로 된 이미지데이터를 파일저장기능을 이용하여 파일로 저장하기.
file = open('Projects/download/aaa.jpg','wb') # write binary mode  , 문서 열었음. 'w' : 글씨 쓰기
file.write(response3.content) # 바이너리 데이터를 파일에 쓰면.. 이게 이미지 파일저장 -> 파일 은 데이타 가지고 있는 덩어리..
file.close()
print('파일 다운로드 성공')
# ------------------------------------------------------------------------

# 다운로드 받은 이미지 데이터를 'aaa.jpg'라는 같은 이름으로 저장하면 덮어쓰기 됨. 
# 그래서 보통 다운로드 할때. 겹치지 않는 이름을 사용함.
# 방법 1) 날짜를 이용하는 방법 'IMG_20260515111042.jpg' 2026-05-15 11:10:42 시간으로 만든 파일명
# 해당 순간의 시간을 기반으로 ...

# 방법 2) 원본파일명(1),원본파일명(2),.[이건 2부수업에서 소개]
address = input('다운로드 하고 싶은 이미지 URL 입력: ')
# https://cdn.pixabay.com/photo/2017/09/08/14/33/lotus-2728884_1280.jpg
response4 = requests.get(address)

# 날짜 정보를 이용하여 중복되지 않는 파일명 만들기.-----
import datetime
#now_data=''
now_data = str(datetime.datetime.now()) 
# Windows는 경로에 특수문자가 있으면 에러.... - : . 띄어쓰기 .. 모두 제거해야 함. 
now_data = now_data.replace('-','')
now_data = now_data.replace(':','')
now_data = now_data.replace('.','')
now_data = now_data.replace(' ','')

#file_name='Projects/download/'+ '20260516' +'.png'
file_name='Projects/download/'+ now_data +'.png'
print(file_name)

# 몇개의 부분만 실행하려면 shift + enter 를 치면 됨. 

# ----------------------------------------------------------------------

#file = open('파일경로/파일명.png','wb') # jpg 손실 압축 , png -> 무손실 압축 (투명 배경을 만들수 잇음. 용량이 더 큼) jpg to png는 손실이 없음. 그 반대는 손실이 있음.
file = open(file_name,'wb') # jpg 손실 압축 , png -> 무손실 압축 (투명 배경을 만들수 잇음. 용량이 더 큼) jpg to png는 손실이 없음. 그 반대는 손실이 있음.

file.write(response4.content)
file.close()

# ---------------------------------------------------------------------------------

# OPEN API 처럼 데이터를 제공해주는 경우도 있지만...
# 필요한 데이터가 OPEN API로 제동되지 않는 경우도 있음.
# 보통 이럴때는 웹 페이지의 내용을 그대로 읽어와서 그 안에서 데이터를 추출함.
# 이를 웹 스크패핑 or 웹 클로링 이라고 부름 ... ( 웹 스프랩핑은 하나를 딱 집어 오는것이고 크롤링은 돌아다니면서 가져오는것)
# 정식 수업은 2부수업에서..
# 이번 시간에는 웹 페이지(문서) 데이터를 읽어오는 맛보기..
# 웹 페이지(문서)는 HTML 이라는 언어로 만들어져 있음. 


# 웹 수업시간에 정식으로 소개예정.
# 이번에는 맛보기...로 HTML를 작성해보면서 웹 페이지를 만드는 모습 경험하고 
# 그 안에서 정보를 추출해보기.

# 웹페이지 만드는 연습 ----- [Web-test]폴더 만들어 .html 문서를 작성해 보기  
# index.html : 대문작 문서.. 즉 대문....
# 웹브라우저 는 HTML을 이쁘게 표시하려고 만듦. 내가 만든 html을 크롬에 드래그 해서 볼수 있음.
#.html .css casecade style sheet 
# 스타일은 css로 만듦. .js : 함수기능

# HTML에서 원하는 정보 추출 실습

#예제1) 아주 간단한 HTML 페이지 분석  -> HTML은 서버에 있음. 
response5 = requests.get('https://mbca2025aix.dothome.co.kr')
print(response5.text)
print()

# 읽어온 HTML 태그를 구별하여 원하는 정보를 추출하는 행위를 part라고 함.
# HTML 태그를 쉽게 해독해주는 외부모듈 사용 BeautifulSoup
# BeatifulSoup(BS) 모듈도 외부모듈이기에 다운로드 및 설치 필요( pip install beautifulsoup4) # 버전. 
# pip list 로 설치된 모듈 볼수 있음.  
#exit으로 나와라.

# BS모듈 사용
from bs4 import BeautifulSoup

# HTML을 파싱하기 위해 위 응답된 HTML 데이타를 BeatifulSoup 객체에게 연결해 주기
soup = BeautifulSoup(response5.text,'html.parser') # 함수가 아닌 다름말임.
# html.parser가 response5.text를 분석해 줄것임.

# soup를 이용하여 원하는 정보를 추출.
# <p>this is my first web server page.</p> p요소 찾아오기
# <p> 요소를 찾아오기
ps = soup.select('p') # 웹 문서에서 모든 'p'요소를 찾아서 리스트로 제공
print('p요소의 개수:',len(ps))

# 요소들의 개수만큼 반복하면서.... 그 안에 써있는 글씨 출력
for p in ps:
    print('p 요소의 글씨:',p.string)

#강사님의 HTML 페이지 'https://mbca2025aix.dothome.co.kr'
# <!DOCTYPE html>
# <html>
#     <head>
#         <title>my web sever</title>
#         <meta charset="UTF-8">

#         <link rel="stylesheet" href="./index.css">
#         <script src="./index.js"></script>
#     </head>
#     <body>
        
#         <h2>MY FIRST WEB SERVER</h2>
#         <p>this is my first web server page.</p>

#         <img src="./image/newyork.jpg" alt="new york image" id="aa">

#         <br>

#         <button onclick="aaa()">이미지 변경</button>


#     </body>
# </html>





# 이미지요소를 찾아소 src 속성의 값을 추출하여 출력(id를 이용하여)
print('이미지 경로:',soup.select_one('#aa').get('src')) #  #이 아이디라는 이야기, #aa 는 aa라는 아이디
print()


#예제2) 실사례.. 오늘의 코스피지수 (네이버 웹페이지에서 정보 추출)
# 소스보기
response6 = requests.get('https://finance.naver.com/sise/sise_index.naver?code=KOSPI')
#print(response6.text)
# BeautifulSoup로 읽어온 웹페이지에서 원하는 코스피 지수를 추출
soup = BeautifulSoup(response6.text,'html.parser')
element = soup.select_one('#now_value') # #아이디:
print('지금의 코스피 지수:', element.string)
# 지금 웹에 있는 자료를 검색해 본것이다... 
#쇼핑몰에서 가격, 가져올수도 있고... 막 가져오면 안됨. 저작권때문에 조심해야 함. 
# 웹에서 데이타를 가져오려면 requests로 요청하고 HTML을 가져오려면 BeatifulSoup가 필요. 
# 그리고 데이타 분석을 하려면 numpy, panda가 필요

#https://cdn.pixabay.com/photo/2017/09/08/14/33/lotus-2728884_1280.jpg
