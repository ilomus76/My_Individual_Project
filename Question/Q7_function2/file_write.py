# 1000명의 이름,키,몸무게 데이타를 만들빈다.

# 랜덤한 숫자를 만들기 위해 가져옵니다. 
import random
# 구글을 통해서 Ghat GPT를 검색해서 들어가 질문에 "python에서 random함수" 라고 치면 해당 함수를 사용하는 방법을 설명해줌.


# 간단한 한글 리스트를 만듭니다.
hanguls = list() # 변수에 리스트함수로 빈문자를 만듦. # hanguls 는 기본자료형의 전역 변수이고 이것은 전역 stack 에 쌓임. 
hanguls = list("가나다라마바사아자차카타파하") # 문자열 이나 대형 데이타를 가져와 리스트로 만들어 줌 . [ "가",'나','다'......]

#file 을 쓰기 모드로 엽니다.
with open('info.txt','w',encoding='UTF-8') as file: # 파일을 쓰기 모드로 설정. # encoding = 'ANSI ' or 'UTF-8'
    for i in range(1000): # range 함수는 어떤 범위의 숫자 시퀀스를 만들어 줌. -> 리스트로 만들어 주는 것은 아님...
        # 숫자 시퀀스에서 값을 가져와서 i에 대입해라
        # 랜덤한 값으로 변수를 생성합니다. 
        name = random.choice(hanguls) + random.choice(hanguls) # 문자열 결합 
        weight = random.randrange(40,100)
        height = random.randrange(140,200)
        # 텍스트를 씁니다.
        file.write("{},{},{}\n".format(name,weight,height))
