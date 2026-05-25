
# 이전에 만든 데이터를 한 줄씩 읽으면서 키와 몸무게로 BMI(비만도)를 계산해 보겠습니다.
with open('info.txt','r',encoding='UTF-8') as file:  # encoding 값이 맞지 않을 경우 error가 날수 있다. 
    for line in file: 
        # 파일 구조에 따라 다르지만 보통 파일을 읽어와서 라인단위로 가져와서 각 라인의 요소를 구하는 것이 일반적이다. 
        # 변수를 선언합니다. -> 해당 변수는 전역 변수로 봐야 하나 아니면 힙에 저장되는 데이타라고 봐야 하나.? 

        # file을 통해 읽는 것은 전부 문자열 데이타이다... 
        (name,weight,height) = line.strip().split(',') # strip()은 각 라인의 양쪽 끝의 빈 자리만 없애는 기능임. 
        # 윗줄의 경우 결과가 리스트로 만들어지고 각 요소가 대입이 되는 것임. 

        # 데이타가 문제없는지 확인합니다 : 문제가 있으면 지나감.
        if (not name) or (not weight) or (not height): # 데이타가 비어있는지 확인
            continue 
        #결과를 계산합니다.
        bmi = int( weight ) / ((int(height)/ 100)**2) 
        result = "" # 빈문자 
        if 25 <= bmi:
            result = "과체중"
        elif 18.5 <=bmi:
            result ="정상 체중"
        else:
            result ="저체중"


        #출력합니다. 
        print('\n'.join(["이름:{}","몸무게:{}","키:{}","BMI:{:.5f}","결과:{}"]).format(name,weight,height,bmi,result))
        print()


