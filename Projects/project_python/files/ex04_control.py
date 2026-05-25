#제어문 : 프로그램의 진행 순서를 제어하는 문법.
# 3종류 : 조건문, 반복문, + 기타제어문 

#1. 조건문 : if , if-else , if-elif
#1) if 
age = 20 # 변수에 값 저장시 자료형 정의됨.
if(age < 20) :    # ; 세미콜론 : 콜론
    print('미성년자 입니다. 시청지도가 필요합니다.') # age < 20 가 참이면 실행
    #if(age<20) 은 들였쓰기 한 곳까지이다.
    #따라서 아래의 들여쓰기 안된곳은 해당 영역이 아님. 
    # if(age < 20):아래에 실행문이 없으면 에러가 남. 

    # #다른언어들 표현 : javescript, c 
    # if(age<20){


    # }

print("여기는 if 문과는 상관없는 실행문입니다.")    

# 조건 영역의 실햄문이 여러줄이어도 됨.

age = 25
if(age <20):
    print('미성년. 시청지도가 필요합니다.')
    print('다른 컨텐츠를 시청하세요.')
    # 문서작성하는 방식과 똑같다.
print('넷플릭스 입니다.') # 이건 IF문과 상관없는 실행문. 들여쓰기가 안되어서...

print()
# ---- End of if


#2) if-else
age = 25
if(age >= 20):
    print("환영입니다. 문 나이트 입니다.")
    print("신나게 즐기세요~~")

    #영역안에 출력기능만 사용가능한 것은 아님.모든 코드 작성 가능함
    n = 10
    n +=20 # n = n + 20 
    print('n:',n)
else: # else 옆에는 조건식이 없다. 쓰면 에러 . if이외의 모든 조건이 else 임
    print("꺼져!!")
    print("좀 커서 와~~~")

#---------- End of if-else ------------------

#2-1) if 문의 중첩 사용 Application 
age =25

if(age< 20):
    print('꺼져!') # Unicode at Python 3.0 [ english == korean]

    if(age>=18):  # if문안에 if문이 있을 수 있다 -> 중첩 if문....
        print('뒷문으로....')
else: # 
    print('성인이시네요. 환영합니다.')

    gender = 'female'
    if(gender == 'female'):
        print('할인해줍니다')
    else:
        print('정가 그대로 ㅜㅜ')

    print("필요한것이 있으면 '찬호박'을 찾아주세요.")

print("지금까지 문나이트 였습니다.")
print()

#-------------- End of application of if-else 


#3) if-elif

score = 75 
if(score >= 90):
    print('A 학점')
    print('아주 우수합니다.')
elif(score >=80): # else if(score >=80):
    print('B학점')
    print("우수합니다.")
elif(score > 70):
    print('C학점')
    print("준수합니다.")
elif(score > 60):
    print('D학점')
    print("분발합시다.")       
else:
    print('F 학점')
    print('거 너무한거 아녀!!!')
print()
#-------------------------------
     
#4) 조건이 2개 이상인 경우 [ and or not : 논리연산자 활용]
#4.1) and : 점수 90이상이고 결석이 1개 이하일때문 A+부여
score = 95
absent_days = 1 # 결석한 일수
if( score >=90 and absent_days <=1):
    print("A+ 학점입니다. 최우수 성적입니다.")
else:
    print("최우수 성적은 될 수 없습니다.")

#4.2) or : 이벤트 당첨조건 - 리뷰를 작성했을때... 
# 특정단어('좋아요')가 있거나 또는
# 최소 20글자 이상 작성한 리뷰 
#review = input('리뷰 입력: ')
review = '오늘 신발이 도착했습니다.'
review = '오늘 신발이 도착했습니다.좋아요'
review = '오늘 신발이 도착했습니다.이거 편하네요. 그리고 빨리 도착했어요. 만족해요.'
if( '좋아요' in review or len(review) >= 20):
    print('이벤트가 당첨~~!!')
else:
    print('탈락!! 원하는 단어가 없거나 글자가 너무 짧아요. ㅜㅜ')
print()

#4.3) not : 나이가 성인이 아니면.... 이라는 조건문구를 그대로 표현.
age = 15
if(not age>20): # age>20 아니면
    print('미성년')
else:
    print('성인')
print()
#-----------------------
#5) 조건식이 크다/작다 만 있지는 않다.. 같다 == 도 많이 사용됨.
#강아지 키우는 게임 : 다마구찌 스타일 게임 만들기
print("@ 강아지 키우기 @")
print("-------------------")
print("1. 밥먹기")
print("2. 산책하기")
print("3. 목욕하기")
print("-----------------")
# menu = input("메뉴선택: ")
menu =1
print() 

#메뉴선택에 따른 처리...
if(menu == '1'):# 문자열입력이기 때문에 if(menu == 1) 하면 안됨.
    print('아구아구..맛있다!!')
elif(menu=='2'):
    print('와우~~신난다~~~~')
elif(menu=='3'):
    print('으아!! 짜증나!!!')
else:
    print('잘못된 메뉴 번호를 입력했습니다.')
print()

# 이런것을 규칙기반 이라고 함. 그래서 if -then 이라고 했음. 

#--------------------------------------------

#6) 특이한 pass 키워드 ( 예약어 ) - 파이썬에서 미리 만들어 놓은 것. 
# 아직 미완성 작업중일때.. 사용  
# 프로젝트를 그룹별로 했을 때 나는 끝났는데 다른 사람이 만든것을 적용할 수 없을때
# 이 코드를 반영하지 못하니 그대로 두면 실행문이 비어 있어 에러가 남. 
a=50
if(a<100):
    print('aaa')
elif(a<200):
    pass # 이건 아무 동작도 하지 않음.. 단지.. 실행문의 위치에 존재할 뿐.. 에러 안나도록...
elif(a<300):
    pass
print()


#7) 조건식을 쓸때 소괄호() 생각 가능 ( 더 많이 사용함)
if a<10: # ()는 생략하되, if에서 한칸을 띄어라.
    print('AAA')
else:
    print('BBB')
print()

# ------------------------------------------

#8) 조건에 따라 실행될 실행문이 한줄이라면..
# 조건식과 실행문을 한줄에 써도 됨(코드의 간결성 때문- One line if문)
#8.1) if 한줄로...
age = 25
if age>20: print('adult') # 실행문이 한줄이기 때문에 가능.
print()                   # 이 print()문은 if와 상관없음. 

#8.2) if-else 한줄로.
#예) 사용자의 숫자가 홀수인지 짝수인지...
#number = int(input('숫자입력:')) # 입력은 문자열이고 그것을 int로 형변환해야 함.
number =10 

# 원래 방법...
if number % 2 == 0 :
    print('even')
else:
    print('odd') 

#한줄로 줄이기..[조심. 순서가 이상함--조건식의 그림을 연상해야 함.]
print('even') if(number%2 == 0) else print('odd') 
# 프린트해 만일 짝수라면,,, 아니면 홀수로 프린트해.... 
# Yes - condition - No 
print()

#8.3) if elif 줄이기 - 형식: 실행문A if(조건1) else 실행문B if(조건2) else 실행문C
menu =4
print('Hello') if(menu==1) else print('Nice') if(menu==2) else print('Good')
#가독성이 떨어짐. 그래서 많이사용하지 않음.
#------------------------------------------------
#9) 위 한줄 줄여쓰기의 특이한 사용 용법 [ 삼항 연산자 : Ternary Operator]
# ( 다른언어에서는 ? :  이라는 삼항 연산자가 별도로 존재)
#예) 사용자가 입력한 2개의 숫자 중 큰 값을 max라는 변수에 저장하기
num1 = 10
num2 = 5

# 방법1) 원래 방법
if num1>num2:
    max_value = num1
else:
    max_value = num2

#print('큰값은:', max_value)

#방법2) 한줄로 줄이기 - 삼항 연산자
max_value = num1 if num1>num2 else num2 # 항이 3개임. 

print('큰값은:', max_value)

# 예2) 조금 더 조건이 많은 경우의 삼항연산자 사용....
# -- 성적에 따라 학점 산출 프로그램. 
score = 75

grade= 'A학점' if(score>=90) else 'B학점' if(score>=80) else 'C학점' if(score>=70) else 'D학점' if(score>=60) else 'F학점'
print('당신의 학점은:', grade)
print()
#--------------------------------

#10) 파이썬은 0과 값이 없는 것을 제외하고는 모두 참 True 로 인식함.
data = 10 # T
data = 0 # F
data = 'hello' #T
data = '' # 빈 문자열 - F
data = [10,20,30] # 다음시간에 배울 리스트! 
data =[] # 빈 리스트 - F
if(data):
    print('참입니다')
else:
    print('거짓입니다.') 

#[사용사례]
# 사용자의 입력이 있는지 확인하기!!
# text = input('글씨를 입력하세요: ')
text = ''
#방법 1)if len(text) > 0: #
#방법 2)if text != '':  
#가장좋은 방법 : 사용자가 입력을 하지 않았을 때...
if not text: 
    print('글씨를 입력하지 않았어요.')
else:
    print('입력한 글씨는: ', text)


# 조건문에서 변수를 사용할 때 주의할 점....
#[1] 특정 조건일때 만 변수값이 변경되는 상황
aa = 'hello'

n =15
if n<10:
    aa='nice'
print('aa변수의 값:',aa)
print()


#[2] 특정 조건일때만 만들어지는 변수를 
# 영역 밖에서 사용하는 문제!!!

# kk = None # 문제해결  
# 값을 대입하지 않으면 에러가 나기 때문에, 값이 없는 것을 넣어 나중에 입력가능.
# n = int(input())
n = 5

if n<10:
    kk= 'good'

print('kk의 값',kk) # kk가 선언이 안되는 경우 이 구문은 에러남..
print()
#-----------------------------------------------------

# while 
# for -in
# 두가지는 호환 가능

#2.반복문 while : 
# ~하는 동안에.... 참인 동안에 계속하고 거짓이 되면 빠져나오게
a = 0     # 무한루프 ctrl+C를 누루면 멈춤 interrupt 거는법 or 휴지통 표시 눌러라.
while(a<5):
    print('aaa')
    #조건식에 사용한 변수의 값을 변경하면...
    #조건 결과가 달라질 수 있음.
    #이를 이용하면..반복 횟수를 제어할 수 있음. 
    a += 1 # a=a+1
print()

# 사례 - 특정 조건을 달성할 때 까지 반복작업 수행...
# [게임의 전투 참여할때 레벨 체크]

level = 5
while ( level <10):
    print('훈련!! 레벨업!',level)
    level +=2 
print('전투 참여!!')
print()

# 반복횟수의 결정은 하나의 코드로 결정되지 않음.
# 1) 제어변수의 초기값
# 2) 제어조건
# 3) 저어변수의 연산
# 위 3개를 모두 고려하여 결정됨...

# 그럼 "Hello" 라는 글씨를 출력하는 실행문을 
# 5번 반복수행하도록 하고 싶다면?...
a=0
while(a<5):
    print('Hello')
    a += 1
print()

a=0
while(a<10):
    print('Hello')
    a += 2
print()


a=5
while(a<10):
    print('Hello')
    a += 1
print()


a=5
while(a>0):
    print('Hello')
    a -= 1
print()

#위 처럼 반복횟수의 결정은 여러방법으로 구현이 가능함..
# Tip. 잘모르겠다면..무조건 초기값은 0.. 조건은 < 횟수.. 연산은 +=1
#----------------------------------

#반복문의 실행문 영역에 print()만 사용가능한 것은 아님. 모든 코드가 가능함.
#키보드 입력도 가능

#예1) 사용자로부터 정수를 5번 입력받으면서 짝/홀 수인지에 대한 판별결과를 출력하기!!

# a = 0

# while(a<5):
#     num = int( input('정수를 입력하세요:') )
#     if num%2 == 0:
#         print("even")
#     else:
#         print("odd")
#     a += 1
# print()


#예2) 사용자로부터 정수를 5번 입력받으면서 그 값들을 모두 더한 누적값(총합)을 출력하기

# total=0 

# a=0
# while(a<5):
#     num= int( input("정수 입력:>"))
#     total += num #total = total +num # 누적합....
#     a+=1

# print('입력된 값의 총 합:',total)
# print('입력된 값의 평균:',total/5) 
# # 성적 프로그램의 알고리즘....

#[참고로 ] 문자열의 결합 +을 이용하여... 문자열을 누적하는 형태도 가능함..
# 오늘의 과제 참조...
ss = ''
ss = ss + "aaa"
ss = ss + "bbb"
ss += "ccc"
print(ss)
# ----------------------------------------------------------

# [다른 사례] 반복에 사용하는 제어변수의 값을 이용할 수도 있음.
n =1 
while(n<10):
    #print(3,"x",n,"=",3*n)
    print("{}x{}={}".format(3,n,3*n)) # f-string이 대세임. 
    n+=1
print()


# [다른 사례] 조건식에 사용하는 값을 변수가 가진 값으로 지정하는 것도 가능
# 사용자가 입력한 숫자만큼 반복하도록.....
# num= int ( input("반복횟수: "))
# a=0
# while(a<num):
#     print('Nice')
#     a+=1
# print()
#---------------------------------------------------

# while 의 조건식을 감싼 소괄호() 생략가능
# -- 대부분 생략 
a = 0
while a<10:
    print("good")
    a+=2
print()
#---------------------------------------------------

# for - in 문 -- 특정 횟수를 반복할때 while 보다 더 간결함. 
# 몇번이라고 정해져 있을때 for, 그런 경우가 아니면 while 을 사용하는게 보통
# 소괄호를 사용하면 에러

#for n in [1,2,3,4,5]: # [] 리스트 안에 있는 요소(값)들을 한번에 하나씩 뽑아서 n 변수에 넣어주면 반복
                      #리스트 , ~에 대하여 ,,, []안에 있는 것을 하나씩 빼와라..
for n in [ 10,20,30,40,50,80,5,13]:
    print()
print()


# 리스트[]의 값을 일일이 나열하기 짜증..
# 그래서 파이썬에 내장된 기능(함수)중에 
# 차례대로 숫자를 만들어주는 range() 함수 이용
# 
#for n in [0,1,2,3,4,5]
for n in range(5): # [0~4] # 5개의 숫자를 만들어줌. 무조건 0부터...
    print(n)
print()

for n in range(5,10): # 5~9 시작, 끝
    print(n)
print()


#2씩 증가하고 싶다면...
for n in range(0,10,2): # start , end전, 간격(step) 0~9까지 2씩...
    print(n)
print()

#반복할 때 숫자가 작아지게 하고 싶다면....
for n in range(10,0,-1): # 10부터 0전까지... 1씩 감소
    print(n)
print()

for n in range(10,0,-3): # 10부터 0전까지... 1씩 감소
    print(n)
print()

# 5단 구구단 출력
dan = 5
for n in range(1,10): # range는 리스트 형태로 만들어줌.
    print(f"{dan}x{n} = {dan*n}")
print()

# 5단 구구단을 역순으로 출력해보기
dan=5
for n in range(9,0,-1):
    print(f"{dan}x{n}={dan*n}")
print()


# 'Hello"라는 글씨를 5번 출력
for n in range(5):
    print("Hello")
print()

#k=int( input())
k=3 
for n in range(k):
    print("Hello")
print()
# ----------------------------

#[응용] 글자수만큼 반복하면서 'GOOD'출력해보기 
word = 'PYTHON' # 띄어쓰기도 글자다
for n in range(len(word)): # 리스트데이타로 만들어줌.
    print("GOOD")
print()

#[별외.] 사실 문자열데이터는 한문자 데이타가 연속으로 배열된...리스트와 같음.
# for 문을 사용할때.. 리스트 자리에.. 문자열 데이타가 있어도 됨. 
for n in word:
    print(n)
print()


s=''
for n in word:
    print(n)
    s +=n # 글자의 누적 연결
print(s)
print()

s=''
for n in word:
    print(n)
    s +=(n+"_") # 글자의 누적 연결
print(s)
print()


# 중첩 반복문..
# 특정 작업을 5번씩 3세트 수행..
# 머신러닝,학습이 이런 작업이다... 
for a in range(3):
    print('세트:',a) 

    for b in range(5):
        print('푸시업:',b+1)
    print()
print()

#중첩 반복문을 이용하여 2~9단까지 모두 출력하기

for dan in range(2,10): # 2단부터 9단까지
    for i in range(1,10): #1~9
        print(dan,"x",i,"=",dan*i)
    print()
print()
#-----------------------------------------
# 분석할 데이타는 엑셀로 되어 있으니 날짜, 상품명등등이 나오니
# 여러줄을 각각 마다마다 하니.
# 총 3줄에 각 라인에 4개씩 있음. 이렇때 쓰는게 중첩이다.

# 프로그램을 하는것은 드라마틱하게 늘어나지 않으니 본인 속도에 맞춰서 최선을 다해라..

#4. 기타 제어문 - break, continue [반복문을 제어하기 위한 제어문 키워드]
# break 멈춰..
for n in range(1,11):
    #특정 조건이 되었을때.. 반복문을 멈추고 싶다면...
    if n==5:
        break # while 문에도 적용 
   
    print("n:",n)
print()

#continue
for n in range(1,11):
    #특정 조건이 되었을때.. 반복문을 멈추고 싶다면...
    if n==5:
        continue # while 문에도 적용 
        #continue : 그 회차가 멈추지만 전체는 멈춘것이 아님.    
    print("n:",n)
print()

## 아래의 것은 continue의 의미가 없음. 멈출려고 하는 행위에 영향을 받는 명령이 없음.
for n in range(1,11):
    #특정 조건이 되었을때.. 반복문을 멈추고 싶다면...
    print("n:",n)
    if n==5:
        continue # while 문에도 적용 
        #continue : 그 회차가 멈추지만 전체는 멈춘것이 아님.        
print()

#[활용 예1] 무한루프를 멈추는 곳에 활용가능.
n = 0
while True:  # 무한루프 
    print("afternoon")
    n+=1
    if n==10:
        break

# [활용2] 사용자로부터 점수를 계속 입력받아...
# 총합을 구하는 프로그램..
# (단, 입력에 -1이 들어오면 종료)

total =0 
while True:
    num= int( input('숫자입력:'))
    if num==-1:
        break
    total = total + num    
print('입력된 값들의 총합:', total) # 코드가 여기까지 도달하지 않을 것이기 때문에 회색으로 변경.


# [활용3] 특정 문자가 입력될때까지 계속 글씨 입력받기
while True:
    word= input('>>>')
    if word== 'exit':
        break

    print('입력된 단어:',word)


# 부트캠프라면 다음주에 코딩 실습만 40문제 품.
# 하지만 우린 부트캠프 아니고 우리는 ai 시대에 살고 있으니 
# 숙달이 아닌 습득이 필요.
