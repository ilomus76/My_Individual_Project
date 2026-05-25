#배치하여 열거하다,놓다.. 이것을 배열이라고 함. array
# 대향의 데이타를 다루는 배열의 필요성.. 확인.

# 왜 필요한가
# 학생 3명 성적데이타 다루기 
student1 = 70
student2 = 80
student3 = 60 

#출력하려면... 각각의 변수명별로 출력해야 함.
print(student1)
print(student2)
print(student3)


#만약, 이런 학생이 20명... 1000명...10000명이면...
# 변수도 20개....출력도 20번 이상.... 직접 작성하는 것 짜증..!!
# 이 점수들을 한번에 묶어서 저장하면.. 더 편하지 않을까...

students = [70, 80, 60]
print(students) # 값들을 알아서 출력.... 2줄만에 출력을 다 함.  

# 값 하나 하나를 뽑아서 사용도 가능..
print(students[0]) 

#반복문을으로 여러개의 요소값 출력가능 
# 배열의 하나하나를 요소 , element라고 부름.

for e in students: # e를 students 라는 배열의 요소를 가져와라...
    print(e)
print()

# ----------------------------------------

# 배열을 통해서 뭔가 편하다는 느낌만 있으면 된다.

# 대부분의 프로그래밍 언어들은 대량의 데이터를 다루는 문법을 배열 Array라고 부름.
# 파이썬은 Array라는 용어를 사용하지 않음. 대신 3가지의 배열 구조를 만들어냄. List, Tuple Dictionary 가 존재함. 
# 리스트는 각각의 변수를 연결하여 만들어 지고 , 인덱스라는 번호를 가지고 있음, 순서대로 저장... 순서에 따라 번호가 저장. 
# 개별 변수들이 체인처럼 저장이 됨. 각 요소가 차례대로 저장됨. 언제든 추가, 삭제 가능. 중간에 삽입도 됨. 체인을 끊고 중간에 넣을 수 잇음.
# 인덱스는 원래대로 써야하고 바꿀수 없음. 해당 요소를 변경도 가능.  

# 튜플은 소괄호.. 체이인 아니라 본드처럼 고정, 추가, 삭제, 값도 바꿀수 없음. 있는 그대로 사용만 할수 있음. 
# 서버에 있는 데이타를 가져왔을 때 실수로 바꿀수 있는 여지를 방지하기 위해서 사용.
# 있는 그대로 써야 함. 
# 만들때만 소괄호이고 사용할 때는 리스트 처럼 인덱싱으로 사용가능.

# 방 번호를 식별자 즉 이름으로 쓰면 알아보기 쉬움. 즉 자동 부여 인덱싱 사용대신 식별자 , 즉 key를 사용하는 것. -> Dictionary
# Key : value 가 쌍으로 이루어 졌다함. 
# 사전을 보면 단어 옆에 값이 있으므로 dictionary라고 붙임. 
# 추가 변경 삽입이 가능. key 만 사용가능

# 0번방, 1변방 , 2번방 이것을 인덱싱 ,,, 딕션너리는 key를 사용.


#1. List [] 대괄호 - 값의 변경 및 요소의 추가/삭제 가능
#2. Tuple () 소괄호- 요소의 값 변경 및 추가/삭제 불가능
#3. Dictionary {} 중괄호 - key : value 쌍으로 요소를 저장 (변경 및 추가/삭제 가능)



#1. List [] 대괄호 - 값의 변경 및 요소의 추가/삭제 가능
aaa = [10,20,30,40] #용어 : 요소 element, 인덱스 index 
print(aaa) # 리스트의 요소값들을 [] 표시하며.. 출력해 줌. 
print( type(aaa)) # 이것은 기본 자료형이 아니어서 < class 'list'> 

# 개별 요소값 사용 - 인덱스 번호 사용
print(aaa[0]) 
print(aaa[1])
print(aaa[2])
print(aaa[3])
#print(aaa[4]) # 존재안함. error  : IndexError: list index out of range
print()

# 요소의 갯수가 많으면 일일이 출력하기 짜증...
# 반복문을 이용하면.. 같으 모양의 출력을 쉽게 처리할 수 있음. 
for n in range(4): # 0,1,2,3
    print(aaa[n])
print()


# for 문은 기본저그올 여러개의 데이터를 요소를 뽑아오는 문벌이어서...
for e in aaa: 
    print(e)

# 각 요소들에 1 더한 값이 출력된 값을 출력해보기
for e in aaa:
    print(e+1)
print()


# 각 요소들의 총합 구하기... [ 예) 성적들의 총점. 평균 구하기...]
#total = aaa[0] +aaa[1] + aaa[2] + ..... # 이렇게 하면 불편함. 

total = 0 
for e in aaa:
    total = total + e 
print('total : ',total)
print()


#2교시
#요소값 변경 --- 요소 1개를 일반 변수처럼 보면 됨... 변수 이름이 인덱스가 있는것처럼 보면 됨.
aaa[0] =100 # 100이 대입
print(aaa) # 값이 바뀌어 출력

# 요소 추가기능 -- append(), 추가하다 , insert() 삽입하다
aaa.append(50) # 리스트 기차의 가장 마지막에 요소 하나가 새로 추가됨.
print(aaa)

# 원하는 위치에 요소 삽입
aaa.insert(0,1000) # 0번방 위치에 1000을 새로 삽입. 기존 요소들은 옆으로 밀림.
print(aaa)


# 요소 삭제 -- remove() 제거하다 , del 키워드 예약어-, clear () -한방에 싹 지워라.
aaa.remove(100) # 100이라는 값을 가진 요소를 제거! 
print(aaa)

del aaa[2] # 2번방 요소를 제거 
print(aaa)

aaa.clear() # 모든 요소 삭제
print(aaa)

#요소의 개수를 알려주는 기능함수 len()
print('요소의 개수:', len(aaa))


# 요소들의 자료형은 서로 달라도 됨.
aaa = [10, 3.14, False , 'sam'] # int ,float , bool , str
print(aaa)

for e in aaa: # aaa안에 있는 각각의 요소에 대하여
    print(e)
print("----------------------------")
print()
# ---------------------------------------------


# 리스트의 여러가지 유용한 기능(function 함수 )들...
#1) 요소의 순서를 뒤집기 -- 원본이 변경됨.  immutable 불변성 , mutable
# 게시글 리스트를 최신글 순으로 보여줄때 활용
aaa.reverse() 
print(aaa)

#2) 요소 정렬
aaa= [4, 15, 7 , 2 , 16,4,10] # 순서가 없음, 문자도 순서화 됨 , 숫자화 되어 있어서.... 
aaa.sort()  # 로또 분석기에 사용
print(aaa)

#3) 요소 중 특정 값의 인덱스 번호(위치) 얻어오기 
print( aaa.index(7))  # sort 되어 인덱스 순서가 바뀌어서 원본값과 다름.

#4) in 연산자로 특정 요소가 있는지 여부(T/F ) 알수 있음. 
print( 7 in aaa)
print(777 in aaa)
print( 777 not in aaa)
print()

#5) 특정 값이 리스트안에 몇개 있는지 카운팅
print(aaa.count(4),"개")


#6) 특정값을 꺼내오기 --- 인덱싱 연산자를 이용한 사용과 다른 것임! 
n = aaa[2] # 이건 사용 
print(n)
print(aaa)

n = aaa.pop(2) # 2번방 요소를 팝콘 튀듯이 꺼내오겠다.  2번방 요소가 꺼내짐. 즉, 리스트에서 제외됨.
print(n)
print(aaa)


#7) 다른 리스트를 내 리스트 뒤에 한방에 추가하는 기능 (리스트의 확장)
aaa = [10,20,30]
bbb = [4,5,6]

#aaa.append() # 값 하나하나 를 추가
aaa.extend(bbb) # 확장하여 늘리다.
print(aaa)

# 리스트의 확장은 매우 많이 사용됨. .extend()기능은 많이 사용 안함. 왜? 
# 리스트도 + 라는 결합 연산자가 제공됨.
# 
ccc = [700,800,900]
print(aaa + ccc)
print()
# ---------------------------------------------------

# 2차원 리스트 --- 리스트의 요소가 또 다른 리스트.... 즉, 리스트 안에 리스트.....
#aaa = [10, 20, 30] 
aaa = [ [10,20,30],['aa','bb'],[3.14, 5.24, 4.33]]
print(aaa)
print(aaa[0])
print(aaa[0][0]) # 0번 차량의 0번 자리
print(aaa[2][1]) # 2번 차량의 1번 자리(좌석)
print()

# len() 의 사이즈를 확인할 때.. 조금 주의할 것..
print(len(aaa),"개")
print(len(aaa[0]),"개") # 4개
print(len(aaa[1]),"개") # 2개
print(len(aaa[2]),"개") # 3개


# 중첩 반복문으로 모든 좌석의 값들 출력해 보기

# aaa에서 각 차량을 가져오고 그 차량에서 각 자리를 가져온다고 보면 되고 실제로 변수를 읽어보면 기차로 연결이 되어 있음.
for row in aaa: # 기차의 한 차량씩....
    for e in row: 
        print(e,end="\t")
    print()
print()

# --------------------

# 리스트를 사용하여 여러데이터를 다루는 예제 2개 소개....
# ex1) 학생 성적들의 촐합과 평균
scores = [ 80, 75, 64, 90,50]
total = 0.

for score in scores:
    total = total + score 
print("총점: ", total )
print("평균: ", total/len(scores))
print()

#ex2) 일주일의 온도 중에서 가장 더운 날의 온도와 요일은?
week_temperature = [14, 12, 15, 19, 14, 7, 10] # 데이타 순서: [월,화,수,목,금,토,일]

# if(week[0]>week[1] & and week[0]>week[2] and week[0]> we)
highest = week_temperature[0]
for temp in week_temperature:
    if temp > highest:
        highest = temp
#기법 = 즉 알고리즘.
# 
print ('최고온도 :',highest)
idx = week_temperature.index(highest) # 가장 높은 온도 19가 있는 곳의 요소 인덱스 번호
print(idx)

if idx==0:
    print("월요일")
elif idx==1:
    print("화요일")
elif idx==2:
    print("수요일")
elif idx==3:
    print("목요일")
elif idx==4:
    print("금요일")
elif idx==5:
    print("토요일")
elif idx==6:
    print("일요일")
print()

# 위 조건문을 더 쉽게...
week= ["월요일","화요일","수요일","목요일","금요일","토요일","일요일"]
print(week[idx])
# ------------------------------------------------------

#지금은 소개 받는 것, 습득은 연습에 , 숙달은 프로젝트에서...

#3교시 
#tuple , dictionary 
#2. Tuple () 소괄호- 요소의 값 변경 및 추가/삭제 불가능
bbb = (10,20,30)
print(bbb)
print(type(bbb)) #<class 'tuple">

# 튜플의 요소값 출력은 리스트와 동일
print(bbb[0])
print(bbb[1])
print(bbb[2])

# 값 변경과 요소 추가/삭제가 불가능
#bbb[0]=100 # error TypeError: 'tuple' object does not support item assignment
#bbb.append(50) # error AttributeError: 'tuple' object has no attribute 'append'

# 특이한 튜플 생성 문법 - 변수 수업에 소개했었음. 
a =10, 20 ,30 # 파인썬에서만 이런 문법이 가능.
bbb = 100,200,300 # 자동으로 () 소괄호로 묶어줌.. 오토박싱기술.
print(bbb)

#반대로.. 튜플의 요소값들을 분해하여 여러변수에 한반에 대입가능 [ 꽤 선호함. 특히 . ML : machine learning 엔지니어]
a,b,c=(100,200,300) # a, b, c는 기본 정수형 변수들...
print(a)
print(b)
print(c)
print("-"*20) # - 문자를 20번 연결
print()
# a,b,c=[100,200,300] # a, b, c는 기본 정수형 변수들... 리스트도 가능.  자바에서 구조할당이라고 함.

# 반복문으로 요소접근하는 것은 당연히 가능.
for e in bbb:
    print(e)
print()
# 튜플은 원본데이타를 실수로라도 건드리지 못하도록 할때 유용하게 활용됨.
#----------------------------------------



#3. Dictionary {} 중괄호 - key : value 쌍으로 요소를 저장 (변경 및 추가/삭제 가능)
ccc = { 'name':'sam', 'age':20, 'address':'seoul'} #식별자는 문자, 숫자.. 숫자를 쓰려면 차라리 리스트를 쓰는게 좋다. 
# 요소 3개.

print(ccc)
print(type(ccc)) # <class 'dict'>

# 요소값 전근은 인덱스번호 대신에... 식별자 Key 사용.
print(ccc['name'])
print(ccc['age'])
print(ccc['address'])

# 리스트처럼 요소의 값 변경 및 추가/삭제 모두 가능
ccc['age']=25
print(ccc)

# 요소 추가...는 
#append 기능은 여기에 인덱스를 줘야 하니 식별자를 넣는 dictionary에는 사용안됨.
ccc['email'] = 'aaa@gmail.com' # 새로운 식별자 key 로 값 대입... 하면 추가됨. 
print(ccc)

#요소 제거
del ccc['email']
print(ccc)

#요소 모두 제거
ccc.clear()
print(ccc)

# in 연산자 활용 - 특정 실별자 key 를 가지고 있는지 확인
ccc = {'name':'sam','age':20, 'address':'seoul'}
if 'name' in ccc:
    print('이름: ', ccc['name'])
# 존재하지 않는 키로 접근하여 당연히 에러...
#print(ccc['tel']) # error

# 키로 접근할때 에러가 걱정된다면... 위 처럼 if문으로 쓰거나...
# 안전하게 값을 얻어오는 기능함수를 사용
value = ccc.get('tel') # 없는 key를 사용하면 None 값을 줌. 에러가 안남.
print(value)

value = ccc.get('address') # 있는 key를 사용하면 그 값을 줌.
print(value)
print()

#딕션너리 요소를 반복무으로 접근하기.. 조금 ..신경써야 함.
#1] 딕션너리에 for in 반복문을 처리하면.. 값이 오지 않고 key 값들이 반복됨.

for key in ccc:
    print(key) # 키 값인. 값이 아님. # name , age, address
print()

#반복되는 key 값을 이용하여 값을 접근.
for key in ccc:
    print(key,":",ccc[key])
print()

#2) key 와 요소값을 한번에 (튜플로) 얻어와서 반복
items = ccc.items()
print(items) # ([('name', 'sam'), ('age', 20), ('address', 'seoul')])

for item in items: # 요소가 3개이니까 3번 돎.
    print(item[0],"-",item[1])
print()

# 위 item은 튜플이기에.. 일반변수들로 분해하여 변수에 넣을 수 있음. 
#for item in items:
for key,value in items:
    print(key, "~",value)
print()
print("~"*20)
print()

# 별외. 리스트의 요소에 또 다른 리스트가능, 튜플,딕션너리도 가능.
ddd = [10,20,30]
ddd = [ [10,20,30],(4,5,6),{'id:':'aaaa','password':'1234'}]
print(ddd)

print(ddd[0][2])
print(ddd[2]['password'])
print("===========================================")
print()

# 4교시
# [추가 !!] 리스트를 만드는 특별한 문법 [ 리스트 내포 list comphreshensions]
# 반복문으로 리스트의 요소를 만들어야 할때...간결하게 한주로 줄여서 쓰는 문법.- 데이터 분석에 많이 사용.

#1] 기존 방식대로 반복문으로 리스트 생성.
aaaa = [1,2,3,4,5,6,7,8,9] # 데이타를 차례대로 만들때가 있다.. x 좌표값을 일정하게 차례대로 해야 할때가 있다.

aaaa=[]  # 빈 리스트를 처음에 한번 만듦.
for n in range(10): # 1~9 , 리스트로 만들어 주지 않음. 
    aaaa.append(n)
print(aaaa) # 생성된 리스트 출력.

#2] 리스트 내포 문법으로 간략화.... 케데헌 같이 말을 줄이자..
bbbb = [ n for n in range(1,10)] # n값으로 채울거야..for문의 n이야. n은 range가 만들어줄거야.
print(bbbb)

# 위 리스트 내포 표현식을 다소 응용하면.....2~10까지의 짝수로... 리스트 생성.
cccc= [ n for n in range(2,11,2)]
print(cccc)

# 위 리스트 내포 표현식을 다소 응용하면.....2~10까지의 짝수의 제곱값들..로 리스트 생성.
cccc= [ n**2 for n in range(2,11,2)]
print(cccc)

#리스트 컴프리헨션 기능은 요소값을 필터기능도 구현 가능함. 걸러내겠다.
#원래 리스트에서 특정 조건의 요소만 뽑아서 새로운 리스트 생성[ 데이타분석에 매우 많이 필요]
scores = [ 70,80,95,42,68,73,57,84]

#60 점 미만을 걸러내고 새로운 리스트 생성..
pass_scores = [score for score in scores if score >= 60] # 사람이었다면 직접 찾아 썼을 것이다.
print(pass_scores)


# (응용) 사용자 입력 숫자만큼 리스트이 요소를 만들기.. 단 , 요소의 초기값을 0으로 설정.
# n = int(input('개수입력: '))
# eee = [ 0 for n in range(n)]  # 상수 입력을 자동으로 넣을 수 있음.
# print(eee) 
print()

# 컴프리헨션 문법이 좀 지저분해서... 별도의 조건없이 간단하게 순서대로 있는 값들로 만든다면...
ggg = list(range(5)) # 리스트 형변환과 비슷 , range(5)를 출력하면 객체라는 말로 나올것임.
print(ggg)

hhh = list(range(2,11,2))
print(hhh)
print('='*30)
print()
#------------------------------------------------

# 4-4 내용
# 리스트로 데이터를 다루면 좋은 점..... 
# 대량의 데이타를 다루는 파이썬 언어에 내장된 함수(기능)의 사용이 가능해 짐.

# 리스트 , 튜플, 딕션너리 등과 관련된 파이썬 내장 함수들(기능)들
#1] 리스트 요소들 중에서 최소, 최대 , 총합 구해주는 파이썬 내장함수 
numbers =[48,107,51,6,786,1024]
print('최소값:',min(numbers))
print('최대값:',max(numbers))
print('총합: ', sum(numbers))
print()

# min, max는 list가 아니어도 값을 여러개 주면 최소/최대값을 구해줌.
print(min(51,75,42,108,53)) 
print(max(51,75,42,108,53))
#print(sum(51,75,42,108,53)) # sum은 안됨. 일반 변수의 sum은 안됨. 리스트만 됨.

#2) 요소들의 순서를 반대로 뒤집기....[reversed()....원본은 불변]
#numbers.reverse() # 원본이 변경됨.
aaaa= reversed(numbers)
print(aaaa) # 뒤집어진 객체 -- 아직 리스트아님. #리스트로 형변환 하면...p
print(list(aaaa))
#원본은 그대로...
print(numbers)


#3] 리스트를 반복문으로 접근할때 인덱스 번호도 같이 표시하고 싶다면?이를 해주는 기능함수
mmm = ['sam','robin','hong']

idx=0
for e in mmm:
    print(idx,":",e)
    idx +=1

#리스트를 반복문으로 접근할때 인덱스 번호도 같이 표시하고 싶다면?이를 해주는 기능함수
mmm = ['sam','robin','hong']
for e in enumerate(mmm): # 이너머레이트.
    print(e)

mmm = ['sam','robin','hong']
for idx,value in enumerate(mmm):
    print(idx,":",value)
print('~~~~~~~~~~~~~')
print()
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~``

# 5교시
#4. Set : 집합 {} -- 서로 다른 데이터를 묶어서 관리하는 문법 [ p515~518]
# 중복된 데이터의 저장을 허용하지 않은....중복데이터는 무시됨. 
# 파이썬 2.8에서 또다른 대량의 데이타가 만들어 짐. set  {} , dictionary와 다른점은 값만 사용한다는 점.
# 딕셔너리처럼 {}중괄호를 사용하지만.. key 식별자를 사용하지 않고.. 값만 나열함.
ddd = { 'sam','robin','park','sam','hong'} # 중복된 'sam'
print(ddd) # 순서대로 저장되어 있지 않음. "중복"된 데이타는 나타나지 않음. 5개를 가지고 있지만... --> 집합.

print(type(ddd)) #<class 'set'>
# 순서가 없기에 인덱스 번호라는 개념도 없음.

# print(ddd[0]) # error 

#for in 문법을 사용하면... 요소별로 접근은 가능함. 
#내부적으로는 해쉬 알고리즘으로 순서를 가져감..
for e in ddd:
    print(e)
print()

#[활용사례] 리스트에서 중복된 요소를 제거할때.. 사용가능
aaa = [10,50,70,80,90,10,50,40,30]
bbb = { e for e in aaa} # set {}에 값들이 나열됨.. 자연스럽게 중복이 제거됨.
print(bbb) # 단, 순서는 바뀔 수 있음. 
print() 
# 중복데이타 방지가 목적


# 수학에서 배웠던...'집합'의 주요 연산자 제공됨.
# 합집합 : | 또는 .union()
aaa = {1,2,3,4}
bbb = {3,4,5,6}
print( aaa | bbb) # 합집합 연산 A U B 
print(aaa.union(bbb)) # {1,2,3,4,5,6}
# 교집합 : & 또는 .intersection()
# 차집합 : - 또는 .difference()

# set 에 대한 내용은 여기서 수업종료... 대신 책이나 검색을 통해 추가내용 확인가능.
# 과제 중 이를 사용하는 문제가 한개 있음.
# 배우지 않은 내용을 해결하는 연습을 해보기... 검색을 통해서... 검색 AI활용

# 오늘 수업 끝...
#지금은 소개 받는 것, 습득은 연습에 , 숙달은 프로젝트에서...


# 수행내역
# chapter4 반복문 - 여기에 List와 dictionary가 소개되어 있음.. 모두 읽기 [~p271]
# p271페이지는 꼭! 읽어보세요... 동기부여...

#과제 
# 1. chapter4[직접 해보는 손 코딩] 따라해 보기
#2. [마무리][도전과제] 수행
#3. [Q5 배열.pdf] 과제 풀이 - 학습하지 않은 내용이 있다면... 검색을 통해 해결....

# 튜플은 5.3장에 소개됨. p 316.




