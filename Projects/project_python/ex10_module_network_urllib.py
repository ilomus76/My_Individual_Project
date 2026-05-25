# 이런 것을 왜 배우냐? 
# 데이터 분석을 통한 서비스를 개발하려면 데이터 수집해야 함. (정식 수업은 2부 수업에서 진행)
# 이 수집할 데이타는 크게 
#1. 회사나 개인이 가진 매출데이터 , 회원데이타, 설문자료 등 엑셀파일같은 형태의 데이터일수도 있고...[파일 입출력 기능사용 ] 
#2. 날씨정보, 채용정보, 행사정보 등 회사나 개인인 가지고 있는 것이 아니라 웹을 통해 서비스 되는 데이터일수도 있음. [ urllib request - 저수준 모듈, 한글이 깨짐, 에러 처리가 안됨 ]
# 이걸 위해서 open 이 아닌 urlopen()을 사용. 
# [urllib request, requests(외부 모듈), BeautifulSoup(외부모듈 , ㅓHTML 분석해 주는것) - 네트워크에 Soup라는 기능이 있었음. ]

# 저수준 레벨 - 개발자가 해야할게 많은 것 , 개발자가 설정할게 많은 것
# 고수준 레벨 - 내부적으로 다 해주는 것, 알아서 해 주는 것. 


#왜부 모듈 , open 소스임. 

# 이렇게 애플리케이션 서비스를 개발할 대 사용할 데이터를 공개해 주는 기술을 OPEN API(Application program interface) 라고 부름 
#그냥 API 는 라이브러리고 Open API는 데이타를 공개했다는 것이다. 

# 웹 데이터를 불러와서 분석하여 원하는 정보를 추출하는 작업이 서비스를 개발할때 거의 필수기술.

# 웹에서 데이타를 가져오는 것.. 
# naver는 정보가 복잡함.
# 간단하게 웹 데이타를 읽어오는 실습을 위한....URL 경로... 이용.

# 강사가 올려준 깃허부 URL
# 표준 모듈을 이용하여 웹 데이터 읽기 구현
from urllib import request

#1] 일반 텍스트 파일 읽기 
address = 'https://raw.githubusercontent.com/2017mrhi/python_network_files/refs/heads/main/aaa.txt' # 주소

url = request.urlopen(address)
data = url.read()
# 어제 했던 파일 입출력 과 같음. close 안해도 됨.

print(data) # 단점 : 한글이 깨져 보임. 아래와 같이
# \n\n\xec\x95\x88\xeb\x85\x95\xed\x95\x98\xec\x84\xb8\xec\x9a\x94.\n\xed\x95\x9c\xea\xb8\x80\xeb\x8f\x84 \xed\x99\x95\xec\x9d\xb8\xed\x95\xb4 \xeb\xb4\x85\xeb\x8b\x88\xeb\x8b\xa4.'
# PS C:\Users\Admin\MBCA\Python> 

# b : binary 
print('-'*30)

#한글을 해독하기 위해 UTF-8 방식으로 해독(디코딩-decoding)해 보겠다.

print(data.decode('UTF-8'))
print('-'*30)
print()
print()

# 실제 웹 데이터들은 보통 표 형태안에 ... 값들이 칸별로 구분되어 존재하는 경우가 많음... (회원정보, 매출데이터, 날짜별 온도... 등)
# 이런 엑셀형태의 파일은 너무 무거워서... 용량이 커서,.. 값들만 추출하여 제공해 줌...
# 추룰하는 실습.
#2] 대량의 데이터를 주는 파일 읽기
address = 'https://raw.githubusercontent.com/2017mrhi/python_network_files/refs/heads/main/bbb.txt' # 주소
url = request.urlopen(address)
data = url.read()
print(data.decode('UTF-8')) 
#sam20AIseoulrobin25DataScienceincheonhong23webdevelopmentbusan
# 위와 같이 읽히면 하나도 구분이 안감. 

# sam 20 AI seoul
# robin 25 Data Science incheon
# hong 23 web development busan
# 위와 같이 띄어 쓰면 데이타의 갯수가 띄어쓰기 때문에 안맞어 분류의 그룹이 어려움. 

# 그래서 콤마로 분리된 값 CSV로 제공함.

print('-'*30)
print()
# 대량의 데이터에서 원하는 정보를 추출하려면....값들의 구분이 용이해야 함.
# 그래서 등장한.. 파일형식..CSV(콤마로 값들을 구분하는 방식, 줄바꿈으로 아이템별 구별)

#3] .csv 파일을 읽어서 원하는 정보를 추출하는 기능 구현...
address = 'https://raw.githubusercontent.com/2017mrhi/python_network_files/refs/heads/main/ddd.csv' # 주소
url = request.urlopen(address)
data = url.read()
print(data.decode('UTF-8'))
print()

#데이타를 수집한다는 것은 단순히... 데이터를 전체를 가져오는 것으로 끝나지 않고..
#그 안에서 원하는 정보를 분리하여 추출할 수 있어야 함.... 

# 이름, 나이, 전공, 주소를 각각 분리해야 함....

# 1) 데이터를 줄 단위로 분리.... --레코드(라인)별 분리.
data = data.decode('UTF-8') # 디코딩된 데이타
lines = data.split('\n')
print('분리된 줄 수: ', len(lines))

# 첫번째 줄은 제목 글씨 줄...이니..이것만 뽑아서 출력.
print('-'*50)
labels = lines[0].split(',') # [ name, age, major , address]
for label in labels:
    print(label,end='\t\t')
print()
print('-'*50)


# 나머지 학생들의 정보도 반복문으로 출력해 보기.
for idx in range(1,len(lines)): #1,2,3
    values = lines[idx].split(',')
    for v in values:
        print(v, end = '\t\t')
    print()
print('-'*50)
print()


# 웹의 존재하는 대량의 데이터는 이런식으로 .csv나 .xml 또는 .json과 같은 파일형식으로 제공함. -내일할 이야기...
# 이 파일형식을 분석(parse)하여 원하는 정보만 뽑아서 분석하는 작업을 해야만 함.
# 


# 대량의 데이터를 줄때 각 값들을 구분하기 위해 사용하는 3가지 데이터 표기형식
# [ 표 형태(tabular)의 데이터를 저장하는 텍스트 파일 형식 ] 1. csv 2. xml 3. json
# 1. csv [comma separated value] 형식
# sam,robin,hong
# 콤마로 구분하여 데이터를 제공 이렇게 콤마로 구분해서 데이터를 쓰고 저장한 파일을 Open API로 제공
# 이 파일의 확장자를 .csv 파일
# [csv 단점] 아이템 1개의 데이터 값이 하나로 이루어져 있지 않음
# 왕십리약국,서울도선동,021234,1025,1700 이수약국,서울사당동,024567 방배약국,서울신림동,0123
# 값들이 콤마로 구분은 되지만 값이 어떤값이지 파악하기 용이하지 않음
# 그래서 csv파일 대신에 다른 표기법을 사용할 필요가 생김. 그래서 채택된 것이 xml 언어의 표기법 사용
# 2. xml [eXtensible markup language]형식
# <OOO></OOO>라는 태그문으로 요소 식별이 가능함..
# 그래서..위 데이터를 xml로 표기해보면.. 어떤 값인지를 파악하기 용이함. <item> <title>왕십리약국</title> <addr>서울시 도선동</addr> <tel>02-214-2356</tel> </item> <item> <title>이수약국</title> <addr>서울시 사당동</addr> <tel>02-456-7892</tel> </item> <item> <title>방배약국</title> <addr>서울시 방배동</addr> <tel>02-447-5567</tel> </item>
# 그래서 거의 2010~2020년까지..(지금까지도) xml로 Open API데이터를 제공하는 기관이 많음.
# 그래서 개발자는 저 위 xml데이터를 사용자에게 그냥 텍스트로 보여주면 못 알아보니 이 xml문서를 분석(parse)해서 이쁘게 화면에 보여주도록 해야 합니다.
# 이 작업을 Open API를 이용한 앱을 만든다 라고 표현함.
# [단점] 지금은 xml이 태그문때문에 너무 문자양이 길어져서 지금은 바꾸는 중.[*개발자의 코드도 좀 지저분함*] 지금은 json 이라는 표기문법을 사용함. - 이게 가장 많이 사용됨
# 3. json [Javascript Object Notation]형식
# [ {"title":"왕십리약국","addr":"서울","tel":1234}, {"title":"이수약국","addr":"인천","tel":8887} ]
# 그래서 기관마다 xml 또는 json 으로 정보를 제공함. 각각의 데이터만 주는 경우도 있고 둘 모두를 제공해 주는 경우도 있음.

# 수행 내역
# 6장은 대략 읽고 넘어가라.
# chapter 7.1까지 했음. 7.1까지 읽기

#과제 
#1.chapter 7.1 [직접 해보는 손 코딩] 따라 코딩하기
#2. chapter 7.2 [마무리]수행 