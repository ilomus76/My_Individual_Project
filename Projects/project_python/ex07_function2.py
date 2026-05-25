# 주요 표준 내장 함수 ( Built-in Function)
# 파이썬에서 제공하는 함수.
#  참고 : 자료는 Admin 밖에서는 사용못하고 Admin안에서만 사용가능.

# 내장함수는 Python 프로그램 작성 시 가장 기본적인고 필수적인 기능을 제공.
# 가장 기초적인 것을 800개 정도 가지고 있음.
# 가장 많이 사용되는 16개정도 소개... 

# 소개 수업이다... 빠르게 살펴보는 느낌. 

#1. print()  : 데이타를 화면에 출력기능. 
#2. input()  : 사용자로 부터 키보드 입력을 받을 수 있는 기능
#3. type()   : 데이타(객체)의 자료형을 리턴해주는 기능 

#4. len()    : 문자열, 리스트 등의 길이나 요소의 개수를 리턴해 주는 기능.

# 문자열 길이
message = 'Hello Python'    # 변수 지정 
print(len(message))  #12

# 요소 개수
aaa= [ 10,20,30]
print(len(aaa))  #3 
aaa.append(40) 
print(len(aaa))  #4

#5. sum() : 숫자 집계, 반복 가능한(for 문으로 돌릴 수 있는 것들) 객체(대량의 데이타-list tuple dictionary)의 모든 요소 합을 리턴해주는 기능 ,  , 튜플 , 리스트 , 딕션너리 

total = sum(aaa) # 리스트 
print(total)

#6. min(), max() : 반복 가능한 데이터나 여러개의 인자(전달값)들 중 최소값, 최대값을 리턴해주는 기능
bbb = [10,72,54,3,180,42,1500]
print(min(bbb))
print(max(bbb))

#7. abs() : absolute 절대적인 ,,, 절대값을 리턴해주는 기능
num =100
print( abs(num))

num =-100     # 위의 변수를 대체 수정.    
print( abs(num))


#8. range() : 지정된 범위의 숫자 시퀀스(순서대로)를 생성해주는 기능.  ( sequential 하다 = 순차적인다.]
aa = range(5) #0 ~4
print(aa) # range 라는 객체(범위를 만들어주는 녀석)가 출력됨.  범위를 만들어 주는 객체
for a in aa: #범위안에 있는 것을 가져온다.
    print(a)

#9. list() : 리스트를 새로 생성하거나. 다른 반복가능한(iterable - for 문에 aa 에 해당하는 것들, list , tuple , dictionary, 문자열) 객체(대량의 데이타)를 리스트형태로 변환해주는 기능
# 리스트를 리스트 혹은 튜플, dictionalry등을 리스트로 , 즉 형변환이다.

my_list=[]  
my_list=list()  #위와 같이 빈 리스트를 만들어줌. 같음.
print(my_list)

# iteralbel 객체를 리스트로 변환 : 문자열, 튜플, 딕션너리, 집합 등을 리스트로.......
aa = list() #리스트로 만들거야.
aa = list("hello")
print(aa) # ['h','e','l','l','o']

bb = list((1,2,3))
print(bb) # [1, 2, 3]

cc = list({'a':10, 'b':20})
print(cc) # 키만 리스트로 만들어서 리턴해 줌 , ['a', 'b']

dd = list({100,200,300}) # 집합 set 
print(dd) # [100, 200, 300] , 순서가 바뀔 수 있음. set은 순서대로 저장되지 않음... 컴퓨터 마다 다를 수 있음. 순서가 정해져 안되어 있는 것이 중요.

#리스트의 연산자 +,*
ee = [10,20,30] + [40,50,60]
print(ee)
print(len(ee)) #6

ee = [10]*5 # 요소값을 반복적으로 추가해 줌. 
print(ee) # [10, 10, 10, 10, 10]

ee = [100,200,300] *5
print(ee) # [100, 200, 300, 100, 200, 300, 100, 200, 300, 100, 200, 300, 100, 200, 300]

ee = [1]*20 + [0]*7 # 1이 20개.. 이어서.. 0이 7개..
print(ee) # [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0] 
#-----------------------------------------------------------------

# 2교시
#10. map() : 반복 가능한 객체의 각 요소에 특정 함수를 적용한 결과를 리턴해준다. 
aaa = [ 10,20,30,40]
# bbb = map ( 특정기능함수, aaa)
bbb = map ( lambda n:n*10, aaa)
print(bbb) # 곧바로 리스트로 결과를 주지않고.. map 책체가 만들어짐. : <map object at 0x00000154A13AF700>
print(list(bbb)) # 리스트로 형변환 # [100, 200, 300, 400]


#11. filter() : map() 처럼 각 요소마다 특정 함수(특정 조건을 결정하는)를 적용한 결과를 리턴해줌. 
# 특정 조건에 해당하는 것만 리턴해준다는 의미. 갯수가 달라질수 있음.

scores = [ 70, 80,40,35,95,72]

# 60점 이상만 뽑아내기...
#pass_scores = filter(특정조건을 가진 함수,scores)
pass_scores = filter( lambda n: n>60 ,scores)
print(pass_scores) # <filter object at 0x00000187A96B6D10>
print(list(pass_scores))  # [70, 80, 95, 72]

#12. sorted() : 반복 가능한 객체 ( 문자열 , 리스트 튜플 딕셔너리)의 정렬된 새 리스트를 리턴해주는 기능 - 원본은 정렬 안됨.
aaa = [10,5,4,8,80,40]
#aaa.sort() # 원본 변경, 나중에 원위치 시킬수 없음. 
bbb = sorted(aaa) # 원본 aaa는 그대로.. 정렬된 새로운 bbb리스트가 만들어짐. 
print(aaa) # [10, 5, 4, 8, 80, 40]
print(bbb) # [4, 5, 8, 10, 40, 80]


#13. enumerate() : 열거하다 ... 반복 가능한 자료형(리스트,튜플, 딕션너리)에 인덱스 번호를 포함하는 튜플로 리턴해 주는 기능
aaa = [10,20,30]
for v in aaa: 
    print(v)

for idx,v in enumerate(aaa): # aaa를 열거해서 안덱스와 값을 묶어서 그 값을 가져와라.
    print(idx,v)

#14. zip() : 묶어주다 , 여러개의 반복 가능한 객체들을 병렬로 묶어 튜플의 반복자로 리턴해주는 기능.
# 데이타가 산재되어 있음. 이름만 정렬, 나이만 정렬된 것들이 있다. 
names = ['sam','robin','hong']
ages = [20,25,30]

#people = [('sam',20)]   -> 리스트로 이미 만들어 짐.
people = zip(names,ages)
print(people) # zip 객체를 출력...   <zip object at 0x000001DD4CE63400>
#리스트로 만들거나.. 또는 .. 반복문으로 묶여진 튜플들을 하나씩 사용 가능

for p in people: # 이미 리스트화 되어 있어 사용 가능.
    print(p)


# ('sam', 20)
# ('robin', 25)
# ('hong', 30)


# 15. int(), float(),str(),bool(), tuple(),dict(),set() 등의 형변환 기능

# 16. any(),all(), : any()는 하나라도 참이면 True 리턴, all()은 모두 참이어야 True
# 예) 요소들 중에서 특정 조건에 해당하는 것이 하나라도 있다면....
scores = [4,8,7,6,3,7,9]
# 특정 점수를 달성하지 못한 값이 하나라도 있나?? 
if any(n<5 for n in scores):
    print('5점을 달성하지 못한 점수가 존재함!!!')    # 5점을 달성하지 못한 점수가 존재함!!!


if all(n<5 for n in scores):
    print('모두 5점을 달성하지 못했어요.')    
else:
    print('일부는 5점 이상을 달성했어요..')  #일부는 5점 이상을 달성했어요..

print("="*30)
print()
# -----------------------------------------------------
# 여기까지 표준함수 종류 알아봄. 


# 표준함수 중에서 데이타분석이나 ML(머신러닝) 작업에서 많이 활용되는 [파일 입출력(처리)] 소개 5.3장에 나옴.
# 프로그램 실행시 RAM에 저장, 휘발성 , 프로그램 끄면 사라짐. 모든 데이타 날라감. 그래서 계산한 값을 디스크로 HDD로 저장.
# 연산은 CPU가 Data는 RAM에 ,,, 영속적으로 데이타를 저장 . HDD 에... 
# RAM은 데이타 형태로 데이타를 가지고 있음. 하지만 HDD는 데이타를 알아보기 위해서 파일 형태로 저장. HDD는 전부 파일 형태로 저장함.
# RAM은 모두 값들만 있음. 파일이 없음. 디스크는 파일 형태로 있음. 파일 이름이 식별자로 알아야 하고 ,, 그것을 실행하기 위해서는 확장자가 있음. 
#글씨로 저장하고 싶으면 txt, 아래한글은 hwp, 엑셀은 xls . 그래서 파일로 저장한다는 것은 별도의 공간에 저장. 근데 파일시스템으로 저장하는데.
# HDD는 데이타를 가지고 있는 파일을 가지고 있는 것임.
# 
# 
# 프로그램이 종료되어도 보관하고 싶은 데이터가 있다면 DISK에 별도의 파일로 저장해야 함. 
# 메모장에서 글자를 쓰면 그것은 RAM에 있는 것이고 그것을 파일로 저장하여 Disk로 저장하는 기능을 위해 프로그램이 Save기능을 넣은 것임.
# 
# 파이썬의 표준함수 중 파일 입출력(저장/읽기) 기능을 아주 쉽게 함수로 제공함. 

#1) 파일에 문자열 데이터를 저장해 보기.
# Data가 HDD로 가기 위한 통로를 stream 이라고 하는데 .. 시냇물이 흘러간다... 뜻 , 한쪽 방향으로 흐름. 즉 한쪽 방향을 내포한 영어단어.
# stream 은 한쪽으로 간다는 것을 내포.
# 내보내는 것인지 받아 들일 것인지 결정해서 내보내야 함. 
# 내보내는 것을 output stream , 받는다는 것을 in stream
# output stream write , input stream 은 read  

# 1) 파일에 문자열 데이터를 저장(파일에 데이터를 쓰는 행위) 해 보기
# open ( " 파일이름","mode")
file =  open ("aaa.txt","w") # mode : 'w:write'덮어쓰기 ,'r::read' , 'a: "append"
# 지금 데이타를 쓸 준비를 한 것임. 한쪽 방향으로..

#이게 글을 쓴것임.
file.write('this is python programming...한글도 되나?')

# 다 쓰면 이것을 닫아야 함.. 안그러면 리소스 낭비가 발생.
file.close()
#---------------------------------------
# file.close()을 하지 않아도 프로그램에 오류는 나지 않음. 다만 리소스가 낭비됨 이것을 메모리 누수라고 함.
# 프로그램에서 file.close()를 하지 않고 종료하게 되면 RAM에 데이타의 리소스가 항상 남아있게 됨. 이런 메모리 누수 - 
# 예전에는 실제로 메모리 누수가 생겼지만 지금은 OS가 알아서 지워줌. 


#3교시
# 파일 경로 
# 저장되는 위치는 파일만 사용했을때 , 원래 파이션의 실행은 CLI ,즉 터미널에서 실행. 그때의 python 명령을 씀. 
# c:// xxxxx / python projects/ex07_function2.py이니 이때 폴더 경로는 xxxx가 됨. 
# 즉 실행 된곳에서 만들어짐.
# 하지만 vS 코드를 사용하다 보니... 그것이 경로를 그대로 가지고 있어 해당 폴더가 동일함.

# vS 코드를 하나 더 열고 그것에서 폴더를 다르게 열어 폴더의 경로에 데이타가 저장됨.

# 파이썬
# 원래 영어 , 하지만 Unicode로 만들었는데 인코딩 방식에 따라 ANSI, UTF-8 로 되는데 그것에 따라 패턴에 따라 보이고 안보이미.
# 메모장에서 저당할 때 UTF-8, ANSI로 저장하는 방법이 있음. 


# #2) 파일 데이터 읽어오기
file = open("aaa.txt","r") # mode : read
#파일을 열때.. 인코딩 방식을 저장할 수 있음. (write도 가능)
#file = open("aaa.txt","r", encoding='UTF-8') # #mode : read , encoding 방식이 다르면 에러...
#데이타를 읽어오는 기능....을 호출하면.. 읽어온 값을 리턴해 줌. 

contents = file.read()
print('읽어온 데이타:', contents)
file.close()   # open 과 close 는 한셋트
#-------------------------


#3)파일 이어쓰기 모드 append mode

file = open('bbb.txt','w') # 덮어쓰기
file.write('aaa')
file.write('bbb')
file.write('ccc')
file.close()
#----------------------
#개행이 되지 않음. 

# 줄바꿈을 하고 싶다면... 데이타를 쓸때(wirte) 줄바꿈문자('\n')도 같이 써야 함. 
file = open('ccc.txt',"a")
file.write('apple\n')
file.write('banana\n')
file.write('orange\n')
file.close()
# 파일에 덮어쓰기 돼고 칸이 개행이 됨. 프로그램을 다시 실행하면 기존에 있는 것들에 이어짐. 

# 인코딩 방식에 대한 확인
file = open('long story.txt','r',encoding ='UTF-16') # 남이 써놓은 글을 읽음. 
contents = file.read()
print(contents)
file.close()
# 한글 글꼴로 에러나는 경우: - encoding ='UTF-16'이 없을 경우
# UnicodeDecodeError: 'cp949' codec can't decode byte 0xff in position 0: illegal multibyte sequence

# 경로 체크해라
#---------------------------------------------------------------


# encoding [ default : ANSI ( 미국 표준협회에서 만든 표준안). 한국어 windows os에서는 ANSI가 CP949로 지정됨.영어권에서는 ANSI.. 유럽은 Windows-1252, 나라마다 다름.]
# 1. UTF-8 : 유니코드 문자 인코딩 방식 중 하나. 가장 널리 사용되는 인코딩. 
# 2. UTF-16 : 유니코드 문자 인코딩 방식 중 하나. 기본문자는 16비트, 그 이상의 문자는 32비트로 인코딩 됨. 
# 3. EUC-KR : 한글 완성형 인코딩, 8비트 문자 인코딩
# 4. CP949  : EUC-KR의 확장 버전 ... 

# ANSI는 영어만 됨. 그걸 한국 OS에서 CP949로 바꾸는 것임. 
#-------------------------------------------------------------------------------


# append mode에 대한 추가 실습
# 사용자로 부터 한줄 리뷰를 계속 입력받아 파일에 저장. 단, 'quit'나가다를 읿력하면 종료하도록...

#file = open('ddd.txt','a',encoding='UTF-8') # 저장할 때 마다 누적됨. 
file = open('ddd.txt','a',encoding='ANSI') # 저장할 때 마다 누적됨.  # 내 피씨는 ANSI가 기본인듯..
while True:
    message = input('리뷰 입력:')
    if message=='quit' or message == '그만':
        print('입력을 종료합니다')
        break
    
    file.write(message +"\n")
file.close()

# 코드에 연연하지 말고 흐름에 집중해라..
#---------------------------------------------------------------------------

#4) 파일 저장 경로(위치) 지정해보기
file = open('projects/files/aaa.txt','w')  # 여기는 python이라는 디렉트리 밑인것임.
file.write('nice to meet you')
file.close()
#쓰기 모드는 파일이 없으면 생성함. 폴더가 없으면 에러! 그래서 미리 폴더를 만들어 놓거나...
#파이썬코드로 폴더를 생성해야 함.( 다음 수업에 배울 모듈개념이 필요함..지금 안함.)

# 파일은 만들어 지는데 경로 폴더가 없으면 에러
# # Traceback (most recent call last):
# #   File "c:\Users\Admin\MBCA\Python\Projects\ex07_function2.py", line 284, in <module>
# #     file = open('projects/file/aaa.txt','w')  # 여기는 python이라는 디렉트리 밑인것임.
# # FileNotFoundError: [Errno 2] No such file or directory: 'projects/file/aaa.txt'


# 4교시
# 상위 폴더 위치 지정하는 상대경로   ../(위에,앞에)    ./ (현재 디렉토리)  상대경로
file = open('../aaa.txt','w')
file.write('have a good day')
file.close()


# 절대경로 지정해보기(권장 안함.. 이유? 개발자 PC 기주이 아니라.. 사용자 PC 기준이기에. 예측어려움)
# 사용자 디렉토리가 맥북일수있고, D 드라이브일수도 있고..
file = open('c:/Users/Admin/aaa.txt','w') # 우리는 admin 계정이라 에러남. C:\Users\Admin 경로부터 사용가능, 다른 바깥쪽은 에러.
file.write('this is good')
file.close()
#--------------------------------------

# #5) 여러중의 문자열도 한번에 파일에 저장할 수 있음. 
file= open('eee.txt','w', encoding='ANSI')
data = '''
안녕하세요.
여러줄의 데이터를 한번에 쓰기
연습해 봅니다.
This is multi lines 
'''
file.write(data)
file.close()
#-------

# #6) 리스트의 데이터들을 파일에 저장하는 것을 한번에 해주는 writelines()
names = ['sam','robin','hong']
file = open('fff.txt','w')
file.close()

names = ['sam','robin','hong']
file= open('fff.txt','w')
file.writelines(names) #이름에 속지 말아요..여러개의 데이터를 줄바꿈해주지 않아요...
file.close()

#-----
#[해결] 리스트의 요소마다 \n을 추가

names = ['sam\n','robin\n','hong\n'] 
#만약 요소 개수가 100개면...\n추가하는 것 짜증..
#실무에서도 데이타마다 \n이 있을리가 없음...
names = ['sam','robin','hong']
#배열의 각 요소마다 \n을 추가해주는 기능함수를 만들어..연결(mapping)해주기
#names = map('\n을 붙여주는 함수',names)
names = map(lambda s:s+'\n',names)

file=open('ggg.txt','w')
file.writelines(names) #이름에 속지 말아요..여러개의 데이터를 줄바꿈해주지 않아요...
file.close()
#-----------

#7) 매일 닫고 닫고 닫고 하는게 귀찮음. 개발자들이 열고 쓰고 닫고를 안하고 , 수많은 작업을 한후 닫기를 안함.
# File 입출력 작업을 안전하게 마치기 위해 close()를 호출해야 하지만 실수로 누락할 여지가 있어서..이를 자동으로 처리해주는 with 키워드.
#file = open ()
with open('hhh.txt','w') as file: # 파일을 열어서.. 파일로서 열어....
    file.write('good day')

# 영역을 벗어나면 자동 close() 됨.
# 또 다른 장점 : 들여쓰기로 인해.. 파일 작업에 관련된 코드들의 구별이 쉬워짐. 
# 실무에서 선호하는 방식... 거의 대부분 이 방식으로 코딩함. 


#8) 파일 데이타를 읽어올때도 당연히 with와 함께.. 좀 긴글을 읽을 때.. 너무 많이 읽어져서 파악이 용이하지 않을 수 있음. 
with open('short story.txt','r',encoding='UTF-8') as file:
    # # 한줄 읽기
    # line = file.readline() # 한줄 읽기
    # print('한줄 문자열:', line)

    # #2]반복문으로 여러줄(10줄) 읽기
    # for i in range(10):
    #     line = file.readline()
    #     print(i,":",line) 

    # #3] 한줄씩 리스트의 요소로 읽어오기 
    # lines = file.readlines() # 리턴: 리스트로 결과를 줌. 
    # print(len(lines))
    # print(lines)  # \n이 보임. 

    #4] file 객체는 반복이 가능한 자료형 ( iterable ) 이기에 이 반복자를 이용하여 한줄씩 쉽게 가능함.
    for line in file: # 파일에서 한줄씩.. 반복처리..
        print(line)
print("="*30)
print()
#--------------------------------------------------------------


# 데이타 분석을 하려면 데이타셋 파일들을 읽어와야 하는데.. 이 파일들이 보통 엑셀형태처럼 표구조가 많다. 
# 이 엑셀 파일을 직접 읽어들이는 기능은..표준함수 open()으로는 불가능[ 셀구조를 이해할 수 없음.]


# 메모장에서 영어는 각 1바이트 ,한글은 3바이트 차지하더라.. 그래서 aI에서는 토큰... 
# 엑셀에서는 영어 저장하니 8.53kbyte 임. 메모장의 사이즈와 엑셀의 사이즈의 차이는 쉘구조때문임. 
# 아래한글도 마찬가지임. a 한글자가 몇 k byte 차지함.
# 만약 엑셀을 읽고 싶다면.. 엑셀에서 셀 구조를 제외한 데이터만 쏙 뽑아서 일반 텍스트파일로 만들어야 함. 이 기능은 다행히.엑셀프로그램에 있어요.
# 각 셀 데이타를 구분하기 위해 콤마로 구분된 형식을 사용하는 .csv 파일형식의 데이타를 많이 사용함. 


#open을 통해서 엑셀은 읽혀지지만 셀구조를 모름.
#셀빼고 데이타만 빼어고 싶다. 
#데이타만 빼오더라도 데이타가 어디서 시작되는지 모름. 
#탭으로 분리하는 저장이 있고 ... 사용자가 저장할때 스페이스 할수도 있음. 
#CSV 쉼표로 분리한 데이타가 있음.  , 로 구분한 데이타... 그리고 행 끝에서 줄바꿈도 들어감. 
# 줄바꿈을 통해서 행을 알수 있고 , 로 열을 알수 있음. 
# 형식을 그냥 txt가 아닌 , 로 분리된 csv coma로 separate된 value 값 csv로 저장. 인터넷때 서버에서 데이타를 받는 방법.
#엑셀파일은 너무 무거우니 이때 데이타를 CSV로 뽑아 줌. CSV가 데이타 형태로 알수 있고 사이즈도 적음. 
# 서버에서 데이타를 저장하는 경우 xls 과 동시에 csv로 제공이 되는 경우 많다. 
# tab으로 분리하는 경우도 tsv tab serapate value 의 확장자로 저장됨. 


#csv를 vsc 에 드래그해서 넣으면 csv를 이쁘게 보여주는 기능을 설치하는 것이 나오는데 이건 끄자.
#이것은 그냥 txt문서이다. 



#9) CSV 파일 데이타를 한줄씩 데이터를 읽어오기
#with open('member.csv','r',encoding='CP949') as file:
#with open('member.csv','r',encoding='UTF-8') as file:
with open('member.csv','r',encoding='ANSI') as file:
    for line in file:
        print('한줄 데이타 :',line)
        # 보통 일반적으로.. 한줄 데이타 'sam,20,seoul'에서 원하는 칸의 값만 뽑아야 하는 경우가 많음. 
        # 콤마, 로 구분된 한줄 데이터를 값별로 분리하기. 작업 수행 (이런것을 CSV파일을 분석한다고 부름.영어로 parsing한다고 부름)
        name , age , address = line.split(',')  # 문자열에서 ,로 분리해서 리스트로 만들어줌.
        print(name, age, address)

        #주의할점. 파일에서 읽어들인 값은 그 생김새와 상관없이 무조건 문자열데이타임. 
        print(type(name),type(age),type(address)) # <class 'str'> <class 'str'> <class 'str'>

        #그래서 age값에 1을 더하고 싶다면... 형변환해서 더해야 함..
        #주의. 데이터셋의 첫줄에 칸이름(column명)이 써있음 '이름,나이,주소' 이건 데이터가 아님..
        #그래서 그냥 int()로 변환하려하면 에러발생

        # 데이터가 누락된 결측치 데이타가 있을 수 있어 이것은 int()형변환 안됨.
        # 가끔 데이타에 앞뒤로 스페이스를 넣은 데이타가 있을 수도 있다. 
        #int()로 바꿀 수 있는 모양새 인지 확인한 후 변환시도....
        
        if age.strip().isdigit(): # 함수 chaiing기법 , isdigit() : 문자열이 숫자로만 이루어 졌는지 여부
            age_int=int(age)
            print(age_int+1) # error - ValueError: invalid literal for int() with base 10: '나이'


print("="*30)
print()
#실무에서 가장 많이 하는 행위중에 하나가 CSV 데이터셋에서 원하는 데이터를 추출하여 분석하는 것임. 
#이를 대략저그올 경험해본 것임.
# 오늘 배운 것중에 9번이 가장 핵심 .
# 오늘 배운것은 다음주 목요일까지 제출해라.

# -----------------------------

#10) mode에 추가된 것들 : + 키워드가 붙어 있음. 
with open('example.txt','w+') as file: # + binary -> 이미지 , 영상 ( + 뭔가 추가,업그레이드 됬다는 뜻) [ write()와 read()둘다 가능]
    # w+,r+,a+ 도 있음. 아주 미묘한 차이 있음.
    #1] 기존 파일을 제거하고 새로 쓰기
    file.write('new data.....')  # 커서가 마지막에 있어서 읽은 것이 없다. 
    # 파일 커서를 첫번째 위치로....
    file.seek(0)
    print(file.read())
      
    #2] 기존 파일을 내용을 유지하면서 파일 끝에 새로운 데이터 추가(파일이 없으면 생성)
with open('example.txt','a+') as file: # 
    file.write('new data.....')  # 커서가 마지막에 있어서 읽은 것이 없다. 
    # 파일 커서를 첫번째 위치로....
    file.seek(0)
    print(file.read())
      

    #3] 기존 파일을 열고.. 수정할 수 있음. 커서의 위치가 처음(파일이 없으면 에러!)
with open('example.txt','r+') as file: 
    file.write('덮어!.')  # 읽어서 커서의 위치가 처음으로 감. 
    # 파일 커서를 첫번째 위치로....
    file.seek(0)
    print(file.read())
      
        